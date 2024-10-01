# Write a program to calculate the factorial of a given number using for loop


# {SPECIAL TIPS: TO INITIALIZE TO PUDUCT WE INITIALIZE WITH 1 AND TO SUM WE INITIALIZE WITH 0}



a= int(input("Enter a number : "))

product = 1
for i in range(1, a+1):
    product = product * i

print(f"The factrorial of {a} is {product}")


