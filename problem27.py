# Write a program to find whether a given number is prime or not.

a= int(input("Enter a number : "))

for i in range(2,a):
    if(a%i == 0):
        print("Entered number is not prime.  ")
        break
else:
    print("Entered number is  Prime.")