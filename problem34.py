# Write a program using functions to find greatest of three numbers.

def greatest(a,b,c):
    if(a>b and a>c):
        print("The greatest number is ",a)
    if(b>a and b>c):
        print("The greatest number is ",b)
    else:
        print("The greatest number is ",c)

def equal_condition(a,b,c):
    if(a==b==c):
        print("All entered numbers are equal.")

a=int(input("Enter the value of first number a "))
b=int(input("Enter the value of second number b "))
c=int(input("Enter the value of third  number c "))

greatest(a,b,c)
equal_condition(a,b,c)

    