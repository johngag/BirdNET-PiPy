"""WSGI entrypoint for production API serving."""

from core.api import create_app

# Gunicorn imports this module and serves `app`.
app, socketio = create_app()
