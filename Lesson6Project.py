import subprocess

devices = []

def AddDevice ():
    name = input("Enter device name: ")
    ip = input("Enter device IP: ")
    mac = input("Enter device MAC: ")
    status = "Down"
    #create device dictionary
    device= {
        "name": name,
        "ip": ip,
        "mac": mac,
        "status": status
    }

    #add to list
    devices.append(device)

def PrintDevices():
    #[{device1},{device2}...]
    for device in devices:
        print("-----------------------")
        print(f"Name: {device["name"]}")
        print(f"IP: {device["ip"]}")
        print(f"MAC: {device["mac"]}")
        print(f"Status: {device["status"]}")

def SearchDevice(name):
    for device in devices:
        if device["name"] == name:
            print("-----------------------")
            print(f"Name: {device["name"]}")
            print(f"IP: {device["ip"]}")
            print(f"MAC: {device["mac"]}")
            print(f"Status: {device["status"]}")
            return
    print("Device not found.")

def RemoveDevice(name):
    #[{device1},{device2}...]
    for device in devices:
        if device["name"] == name:
            devices.remove(device)

def CheckDevices():
    for device in devices:            #the below comment is for windows os
        device_ip = device["ip"]      #-n 1 -w 20
        result = subprocess.run(f"ping -c 1 -W 20 {device_ip}", shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            device["status"] = "Up"
        else:
            device["status"] = "Down"

#main script
while True:
    print()
    print("Menu")
    print("----")
    print("a. Add a device")
    print("b. Display all device")
    print("c. Search for a device by name")
    print("d. Remove a device")
    print("e. Check status for a device")
    print("f. Exit")
    choice = input("Enter your choice: ")

    if choice == "f":
        break
    elif choice == "a":
        AddDevice()
    elif choice == "b":
        PrintDevices()
    elif choice == "c":
        device_name = input("Enter a device name: ")
        SearchDevice(name=device_name)
    elif choice == "d":
        device_name = input("Enter a device name: ")
        RemoveDevice(name=device_name)
    elif choice == "e":
        CheckDevices()