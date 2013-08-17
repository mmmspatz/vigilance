import sqlite3
import datetime
import time
import threading
import os
import requests
from requests import ConnectionError
from config import *



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
    url = "http://" + str(ip) + ":" + str(port) + image_urls[tpe]
    print url
    try:
        r = requests.get(url, timeout=1)#, auth=(username, password))
    except ConnectionError:
        print "Failed to get image"
        return
    print "got image from", devid
    img = r.content
    dt = datetime.datetime.now()
    date = dt.date().isoformat()
    time = dt.time().isoformat()
    directory = content_path + "/" + devid + "/"
    if not os.path.exists(directory):
        os.makedirs(directory)
    fname = directory +date + time + ".jpg"
    f = open(fname, 'w')
    f.write(r.content)
    print "Wrote image to"
    f.close()
    conn = sqlite3.connect(dbname)
    conn.execute("INSERT INTO files VALUES (?, ?, ?)", (devid, fname, dt))
    conn.commit();
    conn.close()
if __name__ == "__main__":
    getIms()
