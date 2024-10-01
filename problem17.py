# Write a program to find the greatest of four numbers entered by the user
a= int(input("enter first number: "))
b= int(input("enter second number: "))
c= int(input("enter third number: "))
d= int(input("enter fourth  number: "))
if(a>b and a>c and a>d):
    print("a is greatest among all: ")
elif(b>a and b>c and b>d):
    print("b is greatest among all: ")
elif(c>a and c>b and c>d):
    print("c  is greatest among all: ",c)
else:
    print("d is greatest among all.",d)
print("END OF PROGRAM  ")



