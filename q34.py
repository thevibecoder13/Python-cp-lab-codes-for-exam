def long_name(text):
    return list(filter(lambda name: len(name) < 5, text))
names = input().split()
result = long_name(names)
print(result)