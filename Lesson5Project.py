import psutil
import subprocess
import nmap

 

#print(psutil.net_if_addrs().keys())
#step 1 get all interfaces
for interface in psutil.net_if_addrs().keys():
    print(interface)

 

#get ip address and subnet mask
interface = input("Choose an interface: ")
ip = psutil.net_if_addrs()[interface][0][1]
mask = psutil.net_if_addrs()[interface][0][2]

 

#get the network id
network_id = ""
for number in range(0,3):
    n = int(ip.split(".")[number]) & int(mask.split(".")[number])
    network_id = network_id + str(n) + "."

 

 

#ping using subprocess Step 4 and Step 5
iplist = []
for host in range(1,5):      #windows ping -n 1 -w 20
    result = subprocess.run(f"ping -c 1 -W 20 {network_id + str(host)}", shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        iplist.append(network_id + str(host))

 

#step 6
print()
print("List of Pingable IP Addresses")
print("-----------------------------")
counter = 1
for ip in iplist:
    print(f"{counter}: {ip}")
    counter = counter + 1
chosen_ip = input("Choose an IP Address: ")

 

#step 7
port_range = input("Enter a port range in the format x-x: ")
port_range = port_range.strip()
ports = port_range.split("-")
if len(ports) != 2:
    print("Two numbers not present in port range")
    exit()
if ports[0].isdigit() == False:
    print("First digit is not a number")
    exit()
if ports[1].isdigit() == False:
    print("Second digit is not a number")
    exit()
if int(ports[0]) < 1 or int(ports[0]) > 65535:
    print("First number out of range")
    exit()
if int(ports[1]) < 1 or int(ports[1]) > 65535:
    print("Second number out of range")
    exit()
if int(ports[0]) >= int(ports[1]):
    print("Second number must be smaller than first number")
    exit()

 

 

#step 8
nm = nmap.PortScanner()
result = nm.scan(chosen_ip, port_range)
print(result["scan"])

 

#step 10
print()
print("Results")
print("-------")
print(f"Host: {chosen_ip}")
print(f"State: {result['scan'][chosen_ip]['status']['state']}")
print("-------")
print("Protocol : tcp")

 

for port_number in result['scan'][chosen_ip]['tcp'].keys():
    print(f"Port: {port_number}, State: {result['scan'][chosen_ip]['tcp'][port_number]['state']}")