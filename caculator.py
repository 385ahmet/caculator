a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")
print("")

c = input("Choose the operation you want to perform: ")

if c == "1":
    print("Result:", a + b)
elif c == "2":
    print("Result:", a - b)
elif c == "3":
    print("Result:", a * b)
elif c == "4":
    if b == 0:
        print("Division by zero error! The second number cannot be 0.")
    else:
        print("Result:", a / b)
else:
    print("Invalid choice!")
