import sqlite3
import datetime
import time
import threading
import os
import requests
from requests import ConnectionError


image_url="/shot.jpg"
video_url="/videofeed"

lighton="/enabletorch"
lightoff="/disabletorch"

port=8080



content_path = "ims/"

username="ryanqputz"
password="crvfty"

updateInterval = 3

def getIms():
    while True:
        print "\n\n\nrunning image loop", threading.current_thread()
        conn = sqlite3.connect('vigilance.db')
        r = conn.execute('SELECT * FROM devices').fetchmany()
        conn.close()
        print "Getting images from:"
        threads = []
        for ip, devid, ping in r:
            threads.append(threading.Thread(target = update, args = (ip, devid)))
        for thread in threads:
            print "starting",  thread
            thread.start()
        for thread in threads:
            print "joining", thread
            thread.join()
        print "done running image loop"
        time.sleep(updateInterval)


def update(ip, devid):
    url = "http://" + str(ip) + ":" + str(port) + image_url
    print url
    try:
        r = requests.get(url)#, auth=(username, password))
    except ConnectionError:
        print "Failed to get image"
        return
    print "got image"
    img = r.content
    dt = datetime.datetime.now()
    date = dt.date().isoformat()
    time = dt.time().isoformat()
    directory = content_path + "/" + devid + "/" + date + "/"
    if not os.path.exists(directory):
        os.makedirs(directory)
    fname = directory + time + ".jpg"
    f = open(fname, 'w')
    f.write(r.content)
    print "Wrote image to"
    f.close()
    conn = sqlite3.connect('vigilance.db')
    conn.execute("INSERT INTO files VALUES (?, ?, ?)", (devid, fname, dt))
    conn.commit();
if __name__ == "__main__":
    getIms()
