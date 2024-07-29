a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")
if operation == '+':
    result = a + b
    print("The result of a+b =" ,result)
elif operation == '-':
    result = a - b
    print("The result is of a-b = ",result)
elif operation == '*':
    result =a * b
    print("The result of a*b = ",result)
elif operation == '/':
        result = a / b
        print("The result of a/b =",result)
else:
    print("Invalid operation")