# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.


m1= "Make a lot of money"
m2= "buy now"
m3= "subscribe this"
m4= "click this"
message= input("enter any comment \n")

if(m1 in message or m2 in message or m3 in message or m4 in message):
    print("This is a spam comment ")
else: 
    print("Thank You  for reaching with us DM for further service: ")
