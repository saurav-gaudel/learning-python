#Write a program to print third, fifth and seventh element from a list using enumerate function.

my_list=[4,5,6,7,10,15,12,11,18]
for i, item in enumerate(my_list):
    if i==3 or i==5 or i==7:
        print(item)

