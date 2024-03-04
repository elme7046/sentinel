import socket
import subprocess
import os

# s = subprocess.check_output("ipconfig")

# #print(s)

# s = s.decode()
# s = s[s.find("Wireless LAN adapter Wi-Fi"):]
# start_line = s.find("IPv4 Address")
# end_line = s[start_line:].find("\n")
# ip_line = s[start_line:(start_line+end_line)]

# ip_index = len(ip_line) - 1

# ip = []
# while(ip_line[ip_index] != ":"):
#     ip.insert(0, ip_line[ip_index])
#     ip_index -= 1
# ip = ''.join(ip)
# ip = ip.strip()
# print(ip)

UDP_IP = "172.20.10.8"
UDP_PORT = 5005
MESSAGE = b"o"

#print("UDP target IP: %s" % UDP_IP)
#print("UDP target port: %s" % UDP_PORT)
#print("message: %s" % MESSAGE)
#sock = socket.socket(socket.AF_INET, # Internet
#                      socket.SOCK_DGRAM) # UDP
#sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

def sendUDP(MESSAGE, UDP_IP, UDP_PORT):
    print("Sending: ", MESSAGE, UDP_IP, UDP_PORT)
    sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

