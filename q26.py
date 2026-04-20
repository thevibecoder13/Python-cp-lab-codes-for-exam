def num_freq(num_lst):
    freq = {}
    for num in num_lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq
text = input("Enter list of numbers: ")
lst = list(map(int,text.split()))
result = num_freq(lst)
print("", result)