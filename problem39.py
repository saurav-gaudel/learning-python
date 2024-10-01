# Write a python function to print multiplication table of a given number.

def multiplication(n):
    for i in range(1,11):
        print(f"{n}*{i}={n*i}")

n=int(input("Enter a number to get multiple of : "))
multiplication(n)
