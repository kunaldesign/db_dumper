# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

#! /usr/bin/python3

import os
import time
import pipes
import datetime


def backup_db(host, user, password, port, name, path):
    DB_HOST = host
    DB_USER = user
    DB_USER_PASSWORD = password
    DB_PORT = port
    DB_NAME = name
    BACKUP_PATH = path

    todays_Date = datetime.date.fromtimestamp(time.time())
    DATETIME = todays_Date.isoformat()

    TODAYBACKUPPATH = BACKUP_PATH + '/' + DATETIME

    try:
        os.stat(TODAYBACKUPPATH)
    except:
        os.mkdir(TODAYBACKUPPATH)

    if os.path.exists(DB_NAME):
        file1 = open(DB_NAME)
        multi = 1
        print("Databases file found...")
        print("Starting backup of all dbs listed in file " + DB_NAME)
    else:
        print("Databases file not found...")
        print("Starting backup of database " + DB_NAME)
        multi = 0

    if multi:
        in_file = open(DB_NAME, "r")
        flength = len(in_file.readlines())
        in_file.close()
        p = 1
        dbfile = open(DB_NAME, "r")

        while p <= flength:
            db = dbfile.readline()
            db = db[:-1]
            dumpcmd = "mysqldump -v -h " + DB_HOST + " --port=" + DB_PORT + " -u " + DB_USER + " -p" + \
                DB_USER_PASSWORD + " " + db + " > " + \
                pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
            os.system(dumpcmd)
            gzipcmd = "gzip " + \
                pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
            os.system(gzipcmd)
            p = p + 1
        dbfile.close()
    else:
        db = DB_NAME
        dumpcmd = "mysqldump -v -h " + DB_HOST + " --port=" + DB_PORT + " -u " + DB_USER + " -p" + \
            DB_USER_PASSWORD + " " + db + " > " + \
            pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
        os.system(dumpcmd)
        gzipcmd = "gzip " + pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
        os.system(gzipcmd)

    print("")
    print("Backup script completed")
    print("Your backups have been created in '" +
          TODAYBACKUPPATH + "' directory")
