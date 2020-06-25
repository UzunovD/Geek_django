#!/bin/bash
mv db.sqlite3 db_backup.sqlite3
python3 manage.py migrate
python3 manage.py loaddata all
