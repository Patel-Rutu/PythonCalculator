#Ask the user to input the first number
num1 = float(input("Enter the first number: "))
#Ask the user to input the operator function they would like to carry between num1 and num2
operator_function = input("Enter the operator (+, -, *, /): ")
#Ask the user to input the second number
num2 = float(input("Enter the second number: "))

#Check which operator was entered
if operator_function == "+":
    #if the operator is "+", then add the first number and second number together
    result = num1 + num2
elif operator_function == '-':
    #if the operator is "-", then substract the second number from the first number
    result = num1 - num2
elif operator_function == "*":
    #if the oprator is "*", then multiply the first and second number together
    result = num1 * num2
elif operator_function == "/":
    #if the operator is "/", then divide the first number by the second number
    result = num1 / num2
else: 
    #if an invalid operator is entered, then print an errod message
    print("Invalid Operator")

#Print the result of the arithmetic operation 
print("Result: ", result)