            
def numberOfTrailingZerosOfAFactorial(number):
        count = 0
        base = 5
        while(base <= number):
            count = count + number//base 
            base = base * 5
        return count

print(numberOfTrailingZerosOfAFactorial(4))
print(numberOfTrailingZerosOfAFactorial(5))
print(numberOfTrailingZerosOfAFactorial(10))
print(numberOfTrailingZerosOfAFactorial(25))
print(numberOfTrailingZerosOfAFactorial(65))
print(numberOfTrailingZerosOfAFactorial(100))