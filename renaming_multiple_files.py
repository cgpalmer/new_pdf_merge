import os

for file in os.listdir("new/"):
    print(file)
    
    os.rename(f"new/{file}", f"test/converted_{file}")

