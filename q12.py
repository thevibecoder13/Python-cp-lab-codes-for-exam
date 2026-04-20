'''12. Write a Python program to remove all vowels from a string using a function.
•	Accept a string from the user. 
•	Create a function that returns the string after removing vowels. 
•	Display the result.
'''
def remove_vowels (text):
    v = "AEIOUaeiou"
    result = ""
    for ch in text:
        if ch not in v:
            result += ch
    return result
sent = input("Enter a sentence: ")
output = remove_vowels(sent)
print("After removing vowels: ", output)