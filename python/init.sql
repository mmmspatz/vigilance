CREATE TABLE devices(ipaddr TEXT UNIQUE, devid TEXT UNIQUE, ping DATETIME, endpoint TEXT);
CREATE TABLE files(devid TEXT, fname TEXT, filetime DATETIME);
CREATE INDEX devid_ind ON files (devid);
CREATE INDEX filetime_ind ON files (filetime);
