import os

network_id = input("Enter a Class C Network ID: ")

for host in range(1,255):
    os.system(f"ping -c 1 {network_id}.{host}")
