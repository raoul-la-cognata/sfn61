#get inputs from user
hostname = input("Enter Hostname: ")
ip = input("Enter IP Address: ")
mask = input("Enter Subnet Mask: ")
department = input("Enter Department: ")
vlan = input("Enter VLAN: ")
 
#remove start and trailing spaces
hostname = hostname.strip()
ip = ip.strip()
mask = mask.strip()
department = department.strip()
vlan = vlan.strip()
 
#The Hostname should be all uppercase and any spaces should be changed to -.
hostname = hostname.upper()
hostname = hostname.replace(" ", "-")
 
 
#comment
comment = "!########################################"
comment = "!" + "#"*40 + "!"
 
#department
department = department.lower()
department = department.replace(" ","_")
 
#MGMT_VLAN, Vlan ID and Department Name
vlan_description = f"MGMT_VLAN_{vlan}_{department}"
 
#ip and mask
ip = ip.replace(" ","")
mask = mask.replace(" ","")

#count number of . in IP and Mask
print(f"Number of . in IP is {ip.count(".")}")
print(f"Number of . in Mask is {mask.count(".")}")

#create Cisco Config
print("Actual Configuration Below")
print("-------------------------")
print("! --- SYSTEM CONFIG ---")
print(f"hostname {hostname}")
print("!")
print("banner motd ^")
print(comment)
print(f"UNAUTHORIZED ACCESS TO {hostname} IS PROHIBITED.")
print(f"CONTACT {department}@company.com FOR ACCESS REQUESTS.")
print(comment)
print("^")
print("!")
print(f"interface Vlan{vlan}")
print(f" description MGMT_VLAN_{vlan}_{department.upper()}")
print(f" ip address {ip} {mask}")
print(" no shutdown")
print("!")
print(" line vty 0  4")
print(" transport input ssh")
print(" login local")
print("!")
print("end")
print("write memory")

