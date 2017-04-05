try:
	mode=int(input("Give me a number! "))
	print("That number was: "),  mode
except ValueError:
	print("That was string without a numeral\n")
except NameError:
	print("That was neither a numeral or a string\n")
