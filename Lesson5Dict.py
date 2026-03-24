#lesson 5 dict
details = {
"name": "David", #key: value
"surname": "Debono",
"course" : "Networking",
"age": 30,
"units": ["Scripting","Virtualisation"]
}
 
print(details)
print(details["age"])
print(details["course"])
 
#print all keys
print(details.keys())
 
#print all values
print(details.values())
 
#change value of age
age = input("Enter your age: ")
details["age"] = age
print(details)
 
#add something new to dictionary
new_key = input("Enter your new key: ")
new_value = input("Enter your new value: ")
details[new_key] = new_value
print(details)
 
#removing a value
details.pop("course")
print(details)
 
#get the value of virtualisation
print(details["units"][1])