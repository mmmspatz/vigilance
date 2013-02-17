from flask import Flask, request
import sqlite3
import requests
from requests import ConnectionError
import datetime
import time
import threading
import os
app = Flask(__name__)

@app.route("/android", methods=['POST'])
def register():
    name = request.data
    ip = request.remote_addr
    print name, ip
    if name == "Invalid":
        return "invalid device name";
    conn = sqlite3.connect('vigilance.db')
    conn.execute("INSERT OR REPLACE INTO devices VALUES (?, ?, time(\"now\"))", (ip, name))
    conn.commit();
    return "got registration"

    


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
