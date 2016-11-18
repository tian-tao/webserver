#/bin/bash
gunicorn app:app -k tornado -b 0.0.0.0:8000
