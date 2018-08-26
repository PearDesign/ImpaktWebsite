import socket

if "impakt" in socket.gethostname():
    from .production import *
else:
    from .local import *
