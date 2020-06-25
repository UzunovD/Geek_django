#!/bin/bash
mkdir ./mainapp/fixtures/
python3 manage.py dumpdata > ./mainapp/fixtures/all.json 
