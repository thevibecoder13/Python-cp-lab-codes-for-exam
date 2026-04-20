def count(text):
    vowels = "aeiouAEIOU"
    v_count = 0
    for ch in text:
        if ch.isalpha():
            if ch in vowels:
                v_count +=1
    return v_count
user_input = input("Enter text: ")
vowels = count(user_input)
print("Number of vowels: ", vowels)