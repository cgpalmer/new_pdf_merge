import os

filename = "test/test1.pdf"
destination = "test/name_changed.pdf"
os.rename(filename, destination)

print("file renamed")
