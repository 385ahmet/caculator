
while True:
  a = int(input("Enter the first number: "))
  b = int(input("Enter the second number: "))

  print("")
  print("1 - Addition")
  print("2 - Subtraction")
  print("3 - Multiplication")
  print("4 - Division")
  print("5 - Compare")
  print("6 - Exit")
  print("")

  c = input("Choose the operation you want to perform: ")

  if c == "1":
    print("Result:", a + b)
  elif c == "2":
    print("Result:", a - b)
  elif c == "3":
    print("Result:", a * b)
  elif c == "4":
    if b != 0:
      print("Result:", a / b)
    else:
      print("Error: Cannot divide by zero!")
  elif c == "5":
    if a > b:
      print(f"{a} is greater than {b}.")
    elif a < b:
      print(f"{a} is less than {b}.")
    else:
      print(f"{a} and {b} are equal.")
  elif c == "6":
    print("Exiting...")
    break
  else:
    print("Invalid operation selected!")
