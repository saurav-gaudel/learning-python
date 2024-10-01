# Write a program to find the sum of first n natural numbers using while loop.

a= int(input("enter any number upto which you should sum : "))

i = 1
sum = 0
while(i<=a):
    sum = sum+i
    i= i+1
    
print(sum)