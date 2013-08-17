import sqlite3
from config import *
import os
import datetime

def clean_files():
    tm = datetime.datetime.now() - image_lifetime
    conn = sqlite3.connect(dbname)    
    oldfiles = conn.execute('SELECT * FROM files WHERE filetime < ?', (tm,)).fetchall()
    for (devid, fname, ftime) in oldfiles:
        try:
            os.remove(fname)
        except OSError:
            pass
    conn.execute('DELETE FROM files WHERE filetime < ?', (tm,))
    conn.commit()
    conn.close()
    
def clean_devices():
    tm = datetime.datetime.now() - device_lifetime
    conn = sqlite3.connect(dbname)    
    conn.execute('DELETE FROM devices WHERE ping < ?', (tm,))
    conn.commit()
    conn.close()    

if __name__ == "__main__":
    clean_files()
    clean_devices()
