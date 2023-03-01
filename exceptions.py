try:
	test = 5/0
except ArithmeticError:
	test = None
else:
	print("No exceptions")
finally:
	print("something important")
print(test)