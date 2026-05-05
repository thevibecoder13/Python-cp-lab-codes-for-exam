import os, sys
with open ("source.txt","r") as f1, open ("destination.txt","w") as f2:
    for line in f1:
        f2.write(line.upper())
    print("file copied in uppercase")