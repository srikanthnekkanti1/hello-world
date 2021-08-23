//This is the code to print the star pattern for a given number of rows
def prnt():

	j = int(input("Enter a number of rows to print: "))

	for x in range(1,j+1):
		i = 1
		print(" "*(j-x), end = " ")
		while i<=x:
			print("*", end = " ")
			i += 1
		print()

	for x in range(1,j+1):
		i = 1
		print(" "*(j-x), end = " ")
		while i<=x:
			print("*"*(j-x), end = " ")
			i += 1
		print()

if __name__ == '__main__':
	prnt()