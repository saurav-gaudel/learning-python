# Write a python function which converts inches to cms.

def inch_to_cm(inch):
    cm=inch*2.54
    print(f"The converted value in cm is : {cm} cm")

inch=int(input("Enter the value to be converted in inches: ")) 
print('inch')
inch_to_cm(inch)