import pyfiglet
import sys
import socket
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

target = input("Enter a remote host to scan: ")
targetIP = socket.gethostbyname(target)

print("-" * 70)
print("Scanning remote host, please wait...", targetIP)
print("-" * 70)

t1 = datetime.now()

try:
	for port in range (1,1025):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = s.connect_ex((targetIP, port))
		if result == 0:
			print("Port {} is open".format(port))
		s.close()

except KeyboardInterrupt:
	print("\n Exiting Program !!!!")
	sys.exit()
except socket.gaierror:
	print("\n Hostname Could Not Be Resolved !!!!")
	sys.exit()
except socket.error:
	print("\n Server not responding !!!!")
	sys.exit

t2 = datetime.now()
total = t2 - t1
print("Scanning completed in: ",  total)
