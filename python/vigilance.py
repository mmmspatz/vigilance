from flask import Flask, request, render_template, url_for, redirect
import sqlite3
import requests
from requests import ConnectionError
import datetime
import time
import threading
import os
from config import *
import json
app = Flask(__name__)

@app.route("/android", methods=['POST'])
def register_android():
    name = request.data
    ip = request.remote_addr
    print name, ip
    if name == "Invalid":
        return "invalid device name";
    print dbname, "android"
    conn = sqlite3.connect(dbname)
    conn.execute("INSERT OR REPLACE INTO devices VALUES (?, ?, datetime(\"now\"), \"android\")", (ip, name.lower()))
    conn.commit()
    conn.close()
    return "got registration"


@app.route("/webcam", methods=['POST'])
def register_webcam():
    name = request.values.keys()[0]
    print request.values.keys()[0]
    ip = request.remote_addr
    print name, ip
    if name == "Invalid":
        return "invalid device name";
    print dbname, "webcam"
    conn = sqlite3.connect(dbname)
    conn.execute("INSERT OR REPLACE INTO devices VALUES (?, ?, datetime(\"now\"), \"webcam\")", (ip, name.lower()))
    conn.commit()
    conn.close()
    return "got registration"


@app.route("/apk")
def getapp():
    return redirect(url_for('static', filename='ptzv.apk'))

#Returns a json object of all device IDs and streams: {'dev1':'url1', 'dev2':'url2', ...} 
@app.route("/streams")
def getstream():
    print dbname
    conn = sqlite3.connect(dbname)
    devs = conn.execute ("SELECT devid, ipaddr, endpoint FROM devices").fetchall()
    d = dict([(i[0], "http://" + i[1] + ":" + str(port) + video_urls[i[2]]) for i in devs])
    conn.close()
    if safeip(request.remote_addr):
        return json.dumps(d)
    else:
        return json.dumps({})

@app.route("/images")
def getnewims():
    conn = sqlite3.connect(dbname)
    devs = conn.execute ("SELECT devid, ipaddr FROM devices").fetchall()
    d = dict([(i[0], "http://" + i[1] + ":" + str(port) + image_urls[i[2]]) for i in devs])
    conn.close()
    return json.dumps(d)    

@app.route("/devids")
def getdevids():
    conn = sqlite3.connect(dbname)
    devices = [i[0] for i in conn.execute("SELECT DISTINCT devid FROM files").fetchall()]
    conn.close()
    return json.dumps(devices)

def safeip(ip):
    return ip[:3] == '18.'

@app.route("/")
def view():
    if request.url_root in full_domains and safeip(request.remote_addr):
        return render_template('streaming.html')
    elif request.url_root in kitchen_domains:
        return viewone('kitchencam')
    elif request.url_root in basha_domains:
        return viewone('webcam')
    else:
        print "not found:", request.url_root
        return viewone('webcam')

@app.route("/single/<devid>")
def viewone(devid):
    ip, tpe = get_ip_type_from_devid(devid)
    print "IP:", ip
    print "devid:", devid
    template = view_templates[tpe]
    return render_template(template, ip=ip, devid=devid)

@app.route("/pan", methods=['POST'])
def pancamera():
    devid = request.form['devid']
    direction = request.form['dir']
    ip, tpe = get_ip_type_from_devid(devid)
    if tpe != 'webcam':
        return "Couldn't move this device"
    try:
        r = requests.get("http://" + ip + ":8080", params={
                'action':'command',
                'plugin':'0',
                'id':'10094852',
                'group':'1',
                'value':direction                    
                })
    except ConnectionError:
        print "Failed to move device"
        return
    return "Moved device"

@app.route("/tilt", methods=['POST'])
def tiltcamera():
    devid = request.form['devid']
    direction = request.form['dir']
    ip, tpe = get_ip_type_from_devid(devid)
    if tpe != 'webcam':
        return "Couldn't move this device"
    try:
        r = requests.get("http://" + ip + ":8080", params={
                'action':'command',
                'plugin':'0',
                'id':'10094853',
                'group':'1',
                'value':direction                    
                })
    except ConnectionError:
        print "Failed to move device"
        return
    return "Moved device"

#http://vigilance.mit.edu:8080/?action=command&dest=0&plugin=0&id=9963776&group=1&value=69
@app.route("/brightness", methods=['POST'])
def setbrightness():
    devid = request.form['devid']
    brightness = request.form['brightness']
    ip, tpe = get_ip_type_from_devid(devid)
    if tpe != 'webcam':
        return "Couldn't set the brightness of this device"
    try:
        r = requests.get("http://" + ip + ":8080", params={
                'action':'command',
                'plugin':'0',
                'id':'9963776',
                'group':'1',
                'value':brightness                    
                })
    except ConnectionError:
        print "Failed to set brightness"
        return
    return "Set brightness"

def get_ip_type_from_devid(devid):
    conn = sqlite3.connect(dbname)
    print devid
    retval = conn.execute ("SELECT ipaddr, endpoint FROM devices WHERE devid==?", (devid,)).fetchone()
    conn.close()
    return retval

@app.route("/archive/<devid>/")
def get_archive(devid):    
    conn = sqlite3.connect(dbname)
    start = request.args['start']
    end = request.args['end']
    r = conn.execute('SELECT fname, filetime FROM files WHERE devid==? AND filetime>datetime(?, \'unixepoch\') AND filetime <datetime(?, \'unixepoch\')', (devid, start, end)).fetchall()
    conn.close()
    return json.dumps(r)


    
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
