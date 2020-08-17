import math

def numberLength(num):
        if(num>9):
            return math.floor(math.log10(num) + 1)
        else:
            return 1

print(numberLength(0))
print(numberLength(10))
print(numberLength(345))
print(numberLength(134567))