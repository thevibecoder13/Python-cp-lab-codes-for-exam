'''6. Write a Python program to count the frequency of each word in a sentence using a function.
•	Accept a sentence from the user. 
•	Create a function that returns a dictionary with word frequencies. 
•	Display the result.
'''
def word_freq(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq
text = input("Enter sentence: ")
result = word_freq(text)
print("", result)