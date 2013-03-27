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
    conn.execute("INSERT OR REPLACE INTO devices VALUES (?, ?, time(\"now\"), \"android\")", (ip, name.lower()))
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
    conn.execute("INSERT OR REPLACE INTO devices VALUES (?, ?, time(\"now\"), \"webcam\")", (ip, name.lower()))
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
    return json.dumps(d)

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

@app.route("/")
def view():
    return render_template('streaming.html')
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
