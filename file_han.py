f = open("data.txt", "r")
text = f.read()
f.close()
length = len(text)
vowels = "aeiouAEIOU"
count = 0
for ch in text:
    if ch in vowels:
        count += 1
print("Length of string:", length)
print("Number of vowels:", count)