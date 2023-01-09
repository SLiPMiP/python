def remove_smallest(numbers):
#     raise NotImplementedError("TODO: remove_smallest")
    smallestNumber=numbers[0]
    indexSlot=0
    for i in range(len(numbers)):
        if numbers[i]<smallestNumber:
            smallestNumber=numbers[i]
            indexSlot=i
    return(indexSlot)

print(remove_smallest([1, 2, 3, 4, 5]))
print(remove_smallest([5, 3, 2, 1, 4]))
print(remove_smallest([1, 2, 3, 1, 1]))
