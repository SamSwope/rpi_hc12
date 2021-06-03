import os

# Function checks to see if file x is in directory d
# x is a string
# Returns True if x is in d, else False
def checkforfile(x, d):
	files = os.listdir(d)
	for f in files:
		if f == x:
			return True
    
	return False
