import socket

if "prod" in socket.gethostname():
    from .production import *
else:
    from .local import *
