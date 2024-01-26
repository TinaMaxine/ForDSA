# Function to check if the parentheses in a string are balanced
def check(str):
	s = []
	for c in str:
		if c == '(':
			s.append('(')
		elif c == ')':
			if len(s) == 0:
				return 0
			else:
				p = s[-1]
				if p == '(':
					s.pop()
				else:
					return 0
	if len(s) == 0:
		return 1
	else:
		return 0


str = input("Please Enter a string to validate")
if check(str) == 0:
	print("Invalid")
else:
	print("Valid")
