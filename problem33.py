# Write a program to print multiplication table of n using for loops in reversed order.

n= int(input("Enter the number to get multilication table: "))

for i in range(10,0,-1):
    print(f"{n}*{i}={n*i}")