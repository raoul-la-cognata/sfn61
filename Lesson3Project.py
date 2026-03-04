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

#check vlan
vlan = int(vlan) #change vlan to an integer from string
if vlan  == 1:
    print("Management VLAN detected.")
    print("WARNING: Using VLAN 1 for management is NOT recommended")
else:
    print("VLAN accepted")

if vlan > 1000:
    print("Extended Range VLAN detected")
 
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
if ip.count(".") != 3: #check if . in ip is not equal to 3
    print("IP does not have 3 dots")
    exit() #stop script

if mask.count(".") !=3:
    print("Mask does not have 3 dots")
    exit()
    
#create Cisco Config
print("Actual Configuration Below")
print("-------------------------")
print("! --- SYSTEM CONFIG ---")
print(f"hostname {hostname}")
print("!")
print("banner motd ^")
print(comment)
if department == "finance":
    print("PROHIBITED")
elif department == "engineering":
    print("TECHNICAL DEPT")
print(f"UNAUTHORIZED ACCESS TO {hostname} IS PROHIBITED.")
print(f"CONTACT {department}@company.com FOR ACCESS REQUESTS.")
print(comment)
print("^")
print("!")
print(f"interface Vlan{vlan}")
print(f" description {vlan_description}")
print(f" ip address {ip} {mask}")
#check if the hostname contains TEST
if hostname.count("TEST") > 0:
    print(" shutdown")
else:
    print(" no shutdown") 

#alternative check if the hostname contains TEST
if "TEST" in hostname:
    print(" shutdown")
else:
    print(" no shutdown")
print("!")
print(" line vty 0  4")
print(" transport input ssh")
print(" login local")
print("!")
print("end")
print("write memory")