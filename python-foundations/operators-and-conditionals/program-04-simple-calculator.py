num1 = int(input("enter  number1:  "))

operator = str(input("enter the operator: "))

num2 = int(input("enter  number2: "))

if operator == "+":

    print(num1 + num2)

elif operator == "-":

    print(num1 - num2)

elif operator == "*":

    print(num1 * num2)

else:

    print(num1 / num2)

print(f" {num1} {operator} {num2}")
