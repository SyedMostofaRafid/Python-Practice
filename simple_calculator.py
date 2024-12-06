num1= float(input("First Digit: " ))
op= (input("Operator(+,-,*,/,%): " ))
num2= float(input("Second Digit: " ))
if op == "+":
    print("Answer is:")
    print(num1+num2)
elif op=="-":
    print("Answer is:")
    print(num1-num2)
elif op=="*":
    print("Answer is:")
    print(num1*num2)
elif op=="/":
    print("Answer is:")
    print(num1/num2)
elif op=="%":
    print("Answer is:")
    print(num1%num2)
else:
    print("Invalid Input")