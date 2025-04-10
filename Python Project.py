#Q1. Write a Python Program to build a simple Calculator?

def Add(Number1, Number2):
    return Number1 + Number2

def Subtract(Number1, Number2):
    return Number1 - Number2

def Multiply(Number1, Number2):
    return Number1 * Number2

def Division(Number1, Number2):
    if Number2 == 0:
        return "Error! Division by zero."
    return Number1 / Number2

def Average(Number1, Number2):
    return (Number1 + Number2) / 2

# User Interface
print("Select an Operation From:")
print("1. Addition")
print("2. Subtract")
print("3. Multiply")
print("4. Division")
print("5. Average")

try:
    select = int(input("Select the Operation from 1,2,3,4,5: "))

    # Convert inputs to numbers
    Number1 = float(input("Enter Your First Number: "))
    Number2 = float(input("Enter Your Second Number: "))

    # Perform selected operation
    if select == 1:
        print(f"{Number1} + {Number2} = {Add(Number1, Number2)}")
    elif select == 2:
        print(f"{Number1} - {Number2} = {Subtract(Number1, Number2)}")
    elif select == 3:
        print(f"{Number1} * {Number2} = {Multiply(Number1, Number2)}")
    elif select == 4:
        print(f"{Number1} / {Number2} = {Division(Number1, Number2)}")
    elif select == 5:
        print(f"({Number1} + {Number2}) / 2 = {Average(Number1, Number2)}")
    else:
        print("Invalid Operation, Please try Again.")

except ValueError:
    print("Invalid input! Please enter numeric values.")



# Q2. Write a Program to check the Username or Password ?

predefined_Username ="Amandubey"
predefined_Password ="Aman@123"

Username= input("Enter Your Username: ")
Password= input("Enter Your Password: ")

if Username == predefined_Username :
    if Password==predefined_Password:
        print("Welcome! Log in was Sucessful")
    else:
        print("Incorrect Password")
else:
    print("Invalid Username")