devices = [] #create an empty list
devices = ["Router1","Router2","Switch1","Firewall1"] #create a list with variables

print(devices[0])
print(devices[2])
print(devices[0:3])

newlist = [1,1.1,"String",True,2] #a list can hold different types of values/variables
print(newlist[1])

print(len(devices))
print(min(devices))
print(max(devices))

#looping through a list
for device in devices:
    print(device)

#adding to a list
d = input("Enter a new value: ")
devices.append(d)
print(devices)

#sorting a list
devices.sort()
print(devices)

#remove from list
devices.remove("Firewall1")
print(devices)

#remove by position
devices.pop(2)
print(devices)

#insert new value
devices.insert(1,"Firewall2")
print(devices)