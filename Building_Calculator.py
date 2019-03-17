#Building Calculator
try:
  while True:
    print("Options")
    print("Enter 'add' to add two numbers")
    print("Enter 'subtract' to subtract two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'divide' to divide two numbers")
    print("Enter 'quit' to end the program")
    user_input = input("")  
    if user_input == "quit":
      break
    print("Enter the first number:")
    a = float(input(""))
    print("Enter the second number:")
    b = float(input(""))  
    if user_input == "add":
      print("Answer is ",a+b)
    elif user_input == "subtract":
      print("Answer is ",a-b)
    elif user_input == "multiply":
      print("Answer is ",a*b) 
    elif user_input == "divide":
      print("Answer is ",a/b)
    else:
      print("Unknown Error")
except ZeroDivisionError:
    print("An error occured")
    print("due to zero division")
