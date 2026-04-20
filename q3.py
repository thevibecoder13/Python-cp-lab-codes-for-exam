'''3. Write a Python program to reverse each word in a sentence using a function.
•	Accept a sentence from the user. 
•	Create a function that returns the sentence with each word reversed but in the original order. 
•	Display the result.
'''
'''
def rev_words(sentence):
    words = sentence.split()
    rev_word = [word[::-1] for word in words]
    return " ".join(rev_word)
text = input("Enter a sentence")
result = rev_words(text)
print("", result)'''
result = " ".join(word[::-1] for word in input().split())
print(result)