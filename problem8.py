# detect double space in program 
name = "Hi, my name is  Saurav Gaudel."
print(name.find("  "))
print(name.find("Gaudel"))
# now to replace double space with single space 
print(name.replace("  "," "))
# here name string is not changed but new modified string of string name is formed that is they are immutable 
