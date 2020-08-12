def palindrome(num):
        rem = 0
        givenNum = num
        while(num > 0):
            rem = rem * 10 + num%10
            num = num//10
        return givenNum == rem

print(palindrome(4553))
print(palindrome(4554))
print(palindrome(0))
print(palindrome(1))
print(palindrome(10))
print(palindrome(101))