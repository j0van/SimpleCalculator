num1 = input("Enter your first number: ")
num2 = input("Enter your second number: ")

print("Type A for addition")
print("Type S for subtraction")
print("Type M for multiplication")
print("Type D for division")
function = input("Select a function: ")
try:
    if function.lower() == "a":
        print("The answer is:",float (num1) + float (num2))
    elif function.lower() == "s":
        print("The answer is:",float (num1) - float (num2))
    elif function.lower() == "m":
        print("The answer is:", float (num1) * float (num2))
    elif function.lower() == "d":
        print("The answer is:", float (num1) / float (num2))
    else:
        print("Invalid input!")
except:
    print("Invalid input!")