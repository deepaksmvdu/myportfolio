import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from cherrypy import wsgiserver

from app import app

if __name__ == "__main__":
    d = wsgiserver.WSGIPathInfoDispatcher({'/': app})
    
    port = int(os.getenv('PORT',8071))
    server = wsgiserver.CherryPyWSGIServer(('0.0.0.0', port), d,numthreads=10,max=-1, request_queue_size=50, timeout=20, shutdown_timeout=10)
    try:
        print "Starting API server on port "+ str(port)
        server.start()
    except KeyboardInterrupt:
        server.stop()
