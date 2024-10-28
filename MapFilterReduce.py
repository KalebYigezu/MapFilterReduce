from functools import reduce



nums = [0,1,2,3,4,5,6,7,8,9,10]

evens = list(filter(lambda x: x % 2 == 0, nums))

divide = list(map(lambda x: int(x / 2), evens))

sum = reduce(lambda x, y: x + y, divide)

print("Nums :  ", nums)
print("Evens :  ",evens)
print("Divide :  ",divide)
print("Sum :  ",sum)

------------------------------------------------------

from functools import reduce

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def even(n):
    if n % 2 == 0:
        return n
    else:
        return n + 1

def gfive(n):
    if n > 5:
        return 1

def add(x, y):
    return x + y


mo = list(map(even, l))
print("Even = ", mo)

fo = list(filter(gfive, mo))
print("Greater Than = ", fo)

ro = reduce(add, fo)
print(ro)
