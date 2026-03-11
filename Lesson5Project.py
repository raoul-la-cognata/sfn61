import psutil
 
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
for number in range(0,4):
    n = int(ip.split(".")[number]) & int(mask.split(".")[number])
    network_id = network_id + str(n) + "."
 
network_id = network_id[0:len(network_id)-1]
print(network_id)