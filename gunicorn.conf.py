# gunicorn.conf.py

bind = "0.0.0.0:8000"
workers = 3  # Adjust as needed
worker_class = "sync"
timeout = 30
loglevel = "info"
wsgi_app = "app:server" #replace app with your filename, and server with your flask server object.