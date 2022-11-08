import sys

filename = input("Enter the name of the file to save to: ") + ".txt"

with open(filename, 'w') as sys.stdout:		  # Open a file with the name supplied by the user.
	for i in range(16777216):			  # The range of possible 26-bit combinations.
		print(hex(i)[2:].zfill(6).upper()) # Change the zfill number to change the number of hex chars. 
							  # If you do, make sure to change the range accordingly!
