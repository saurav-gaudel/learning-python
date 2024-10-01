# write a program to get marks of students and print in sorted manner
marks= []
m1= int(input("Enter marks1 : "))
marks.append(m1)
m2= int(input("Enter marks2 : "))
marks.append(m2)
m3= int(input("Enter marks3 : "))
marks.append(m3)
m4= int(input("Enter marks4 : "))
marks.append(m4)
marks.sort()
print(marks)
# can be sorted by only changing data type to int as it is in default in string 