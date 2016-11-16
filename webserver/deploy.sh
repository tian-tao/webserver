#/bin/bash
gunicorn app:app -k tornado
