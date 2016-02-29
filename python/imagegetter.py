import sqlite3
import datetime
import time
import threading
import os
import requests
from requests import ConnectionError
from config import *

def dir(devname):
    t = datetime.datetime.now()
    return (devname + "/" + t.date().isoformat() + "/" + str(t.hour).zfill(2) + "/", str(t.minute).zfill(2) +":" + str(t.second).zfill(2) + ".jpg", t)

def getIms():
    while True:
        start = time.time()
        conn = sqlite3.connect(dbname)
        r = conn.execute('SELECT ipaddr, devid, ping, endpoint FROM devices').fetchall()
        conn.close()
        threads = []
        for ip, devid, ping, tpe in r:
            threads.append(threading.Thread(target = update, args = (ip, devid, tpe)))
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        dt = updateInterval - (time.time() - start)
        if dt > 0:
            time.sleep(dt)


def update(ip, devid, tpe):
    if ip[0:5] == "http:":
        url = str(ip) + ":" + str(ports[tpe]) + image_urls[tpe]
    else:
        url = "http://" + str(ip) + ":" + str(ports[tpe]) + image_urls[tpe]
    print url
    try:
        r = requests.get(url, timeout=1)
    except ConnectionError:
        print "Failed to get image"
        return
    print "got image from", devid
    try:
        img = r.content
    except Exception:
        return
    d, fname, dt = dir(devid)
    directory = content_path + d
    if not os.path.exists(directory):
        os.makedirs(directory)
    fname = directory + fname
    f = open(fname, 'w')
    f.write(r.content)
    print "Wrote image to", fname
    f.close()
    conn = sqlite3.connect(dbname)
    conn.execute("INSERT INTO files VALUES (?, ?, ?)", (devid, fname, dt))
    conn.commit();
    conn.close()
if __name__ == "__main__":
    getIms()
