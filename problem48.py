from functools import reduce
# Map Example
l= [1,2,3,4,5]
square = lambda x: x*x
sqlist = map(square, l)
print(list(sqlist))


#filter Example
def even(n):
    if n%2==0:
        return True
    return False

onlyEven = filter(even, l)
print(list(onlyEven))

#reduce example 
def sum(a,b):
    return a+b

multiple= lambda a,b: a*b
print(reduce(sum,l))
print(reduce(multiple,l))

