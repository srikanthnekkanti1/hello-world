//This is the code to print the star pattern for a given number of rows
//We can leverage this code to print the numbers also in patterns
def prnt():

	//Entering the rows to print
	j = int(input("Enter a number of rows to print: "))

	//Top Triangle loop
	for x in range(1,j+1):
		i = 1
		print(" "*(j-x), end = " ")
		while i<=x:
			print("*", end = " ")
			i += 1
		print()

	//Bottom Triangle loop
	for x in range(1,j+1):
		i = 1
		print(" "*(j-x), end = " ")
		while i<=x:
			print("*"*(j-x), end = " ")
			i += 1
		print()
	
	//Do we need both the patterns of the traingle??

if __name__ == '__main__':
	prnt()