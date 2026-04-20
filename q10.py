'''10. Write a Python program to find common elements between two lists using a function.
•	Accept two lists from the user. 
•	Create a function that returns a list of common elements. 
•	Display the result.
'''
def common_elements(list1, list2):
    result = []
    
    for item in list1:
        if item in list2 and item not in result:
            result.append(item)
    return result
list1 = list(map(int, input("Enter first list (space-separated): ").split()))
list2 = list(map(int, input("Enter second list (space-separated): ").split()))
common = common_elements(list1, list2)
print("Common elements are:")
print(common)