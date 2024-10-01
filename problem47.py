#Store the multiplication tables generated in problem 45 in a file named Tables.txt

a= int(input("Enter a number :  "))
table=[a*i for i in range(1, 11)]
with open( "table.txt","a") as f:
    f.write(str(table) + "\n")
