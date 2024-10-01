#Write a list comprehension to print a list which contains the multiplication table of a user entered number.


a=  int(input("Enter a number:"))

table=[a*i for i in range(0,11)]
print(table)