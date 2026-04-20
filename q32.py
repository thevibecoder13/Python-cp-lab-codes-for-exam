def second_largest(lst):
    lst = list(set(lst))    
    if len(lst) < 2:
        return "No second largest element"
    
    lst.sort()
    return lst[-2]
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
result = second_largest(numbers)
print("Second largest number:", result)