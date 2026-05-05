f1 = open("file1.txt", "r")
f2 = open("file2.txt", "r")
f3 = open("merged.txt", "w")

lines1 = f1.readlines()
lines2 = f2.readlines()

max_len = max(len(lines1), len(lines2))

for i in range(max_len):
    if i < len(lines1):
        f3.write(lines1[i])
    if i < len(lines2):
        f3.write(lines2[i])

f1.close()
f2.close()
f3.close()

print("Files merged successfully.")