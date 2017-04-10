import socket
import os
HOST,PORT = "localhost",8080

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

