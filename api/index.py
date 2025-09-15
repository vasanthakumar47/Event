# api/index.py
# Ensure parent (repo root) is on sys.path so we can import app.py
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import app as application  # Flask instance in app.py
app = application  # expose both names for safety
