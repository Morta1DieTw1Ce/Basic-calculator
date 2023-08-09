
print("\n BASIC CALCULATOR\n")

print("Enter your first no:")
n1 = int(input()) 

print("Enter your first no:")
n2 = int(input())

print("Enter a operator(+,-,*,/)")
op = input()

if op == "+":
	ans = n1 + n2
	print("Your answer:",ans )
elif  op == "-":
	ans = n1 - n2
	print("Your answer:",ans )
elif op == "*":
	ans = n1 * n2
	print("Your answer:",ans )
elif op == "/":
	ans = n1 / n2
	print("Your answer:",ans )
else:
	print("Wrong operator!")