try:
	mode=int(raw_input("Say Hi to whom? "))
except ValueError:
	print("This is not a number")
print("Hello world from Travis CI")