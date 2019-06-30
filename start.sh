#!/bin/bash
gunicorn -c gunicorn.py manager:app
#python3 manager.py runserver
