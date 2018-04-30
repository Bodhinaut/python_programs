while True:
    print("Options: ")
    print("Enter 'add' to add two numbers")
    print("Enter 'subtract' to subtract two numbers.")
    print("Enter 'multiply' to multiply two numbers.")
    print("Enter 'divide' to divide two numbers.")
    print("Enter 'square' to square two numbers.")
    print("Enter 'quit' to end the program.")
    user_input = input(": ")

    if user_input == "quit":
        print("Thanks a ton for using Simple'Cal, have a great day! :)")
        break
    elif user_input == "add":
        num1 = float(input("Enter a number: ") )
        num2 = float(input("Enter a number: ") )
        result = str(num1 + num2)
        print("The answer is " + result)
    elif user_input == "subtract":
        num1 = float(input("Enter a number: ") )
        num2 = float(input("Enter a number: ") )
        result = str(num1 - num2)
        print("The answer is " + result)
    elif user_input == "multiply":
        num1 = float(input("Enter a number: ") )
        num2 = float(input("Enter a number: ") )
        result = str(num1 * num2)
        print("The answer is " + result)
    elif user_input == "divide":
        num1 = float(input("Enter a number: ") )
        num2 = float(input("Enter a number: ") )
        result = str(num1 / num2)
        print("The answer is " + result)
    elif user_input == "square":
        num1 = float(input("Enter a number: ") )
        result = str(num1 * num1)
        print("The answer is " + result)

    else:
        print("Unknown input.")
