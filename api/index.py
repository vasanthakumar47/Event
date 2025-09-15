# api/index.py
# Vercel auto-detects a WSGI app if you expose `app` (or `application`)
from app import app as app
application = app  # export both names for safety
