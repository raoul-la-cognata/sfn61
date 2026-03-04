ip = input("Enter and IP Address: ")

#get first octet
octet = ip.split(".")[0]

octet = int(octet)  

if octet >= 1 and octet <= 126:
    print("Class A")
elif octet >= 128 and octet <= 191:
    print("Class B")
elif octet >= 192 and octet <= 223:
    print("Class C")
elif octet >= 224 and octet <= 255:
    print("Class D")
else:
    print("Invalid")

print(octet)
