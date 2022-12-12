import socket
import re

ip_address = socket.gethostbyname(socket.gethostname())

vulnerable_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 1433, 1521, 3306, 3389]

print("Port | Zafiyet Durumu")
print("-------------------")

for port in vulnerable_ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ip_address, port))

    if result == 0:
        status = "Açık"
        print("\033[31m{} | {}".format(port, status))
    else:
        status = "Kapalı"
        print("{} | {}".format(port, status))

    sock.close()
