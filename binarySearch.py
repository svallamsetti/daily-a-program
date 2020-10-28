def binary_search(givenList, searchItem):
    low = 0
    high = len(givenList) - 1
    while(low <= high):
        mid = (low + high) // 2
        guess = givenList[mid]
        if(guess == searchItem):
            return mid
        if(guess > searchItem):
            high = mid - 1
        else:
            low = mid + 1
    return
    
print(binary_search([0,1], 1))    
print(binary_search([10,11,12,13,14,15], 16))
