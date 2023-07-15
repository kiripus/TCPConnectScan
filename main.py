#!/usr/bin/env python3
import sys
import socket

ip = sys.argv[1]
ports = sys.argv[2]
port_list = ports.split(",")
for port in port_list:
    if isinstance(port, str):
        port_range = port.split("-")
        if len(port_range) == 2:
            port_list.remove(port)
            for i in range(int(port_range[0]), int(port_range[1]) + 1):
                port_list.append(str(i))

for port in port_list:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        s.connect((ip, int(port)))
        print("Port " + port + " is open")
        s.close()
    except socket.timeout:
        print("Port " + port + " is filtered")
        s.close()
    except:
        print("Port " + port + " is closed")
        s.close()


