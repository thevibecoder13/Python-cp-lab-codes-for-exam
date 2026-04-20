'''4. Write a Python program to count the number of vowels and consonants in a string using a function.
•	Accept a string from the user. 
•	Create a function that returns both counts. 
•	Display the result.
'''
def count(text):
    vowels = "aeiouAEIOU"
    v_count = 0
    c_count = 0
    for ch in text:
        if ch.isalpha():
            if ch in vowels:
                v_count +=1
            if ch not in vowels:
                c_count +=1
    return v_count, c_count
user_input = input("Enter text: ")
vowels, consonants = count(user_input)
print("Number of vowels: ", vowels)
print("Number of consonants: ",consonants)