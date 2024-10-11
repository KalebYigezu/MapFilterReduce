from functools import reduce



nums = [0,1,2,3,4,5,6,7,8,9,10]

evens = list(filter(lambda x: x % 2 == 0, nums))

divide = list(map(lambda x: int(x / 2), evens))

sum = reduce(lambda x, y: x + y, divide)

print("Nums :  ", nums)
print("Evens :  ",evens)
print("Divide :  ",divide)
print("Sum :  ",sum)
