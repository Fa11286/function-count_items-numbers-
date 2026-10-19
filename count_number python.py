def count_items(numbers):
    counts = {}
    for num in numbers:
        if num in counts:
            counts[num] = counts[num]+1
        else:    
            counts[num] = 1
    return counts

numbers = input("Enter your numbers : ")
numbers = numbers.split()

print(count_items(numbers))
