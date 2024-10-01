# Write a python program using function to convert Celsius to Fahrenheit.

def convert(c):
    f= c*(9/5)+32
    return f

c=int(input("Enter temperature in degree celsious:"))
f= convert(c)
print(f"Temperature in fahrenheite is : {f}")

    