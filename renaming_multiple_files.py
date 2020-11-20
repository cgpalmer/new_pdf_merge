import os

for file in os.listdir("new/"):
	os.rename(file, f"new/converted_{file}")
