#1. Add
#2. Subtract
#3. Multiply
#4. Divide
#5. Square root

print("Select an operation to carry out:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. modulus")
print("6. floor division")

operation = input()
if operation == "1":
   num1 = input("Enter number 1: ")
   num2 = input("Enter number 2: ")
   print("The sum is" + str(int(num1) + int(num2)))
elif operation == "2":
    num1 = input("Enter number 1: ")
    num2 = input("Enter number 2: ")
    print("The difference is" + str(int(num1) - int(num2)))
elif operation == "3":
    num1 = input("Enter number 1: ")
    num2 = input("Enter number 2: ")
    print("The product is" + str(int(num1) * int(num2)))
elif operation == "4":
    num1 = input("Enter number 1: ")
    num2 = input("Enter number 2: ")
    print("The result is" + str(int(num1) / int(num2)))
elif operation == "5":
    num1 = input("Enter number 1: ")
    num2 = input("Enter number 2: ")
    print("The modulus is" + str(int(num1) % int(num2)))
elif operation == "6":
    num1 = input("Enter number 1: ")
    num2 = input("Enter number2: ")
    print("The floor division is" + str(int(num1) // int(num2)))
else:
    print("Invalid Entry")