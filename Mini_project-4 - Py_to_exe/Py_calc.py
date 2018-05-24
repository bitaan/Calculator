import math
def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mult(a,b):
    return a * b

def div(a,b):
    return a / b

def power(a,b):
    return(math.pow(a,b))

def root(a):
    return(math.sqrt(a))

while True:
    print('''Enter what type of calculation you want to perform:
             1 for Addition
             2 for Subtraction
             3 for Multiplication
             4 for Division
             5 for Exponential
             6 for Square root''')
    try:
        choice = int(input("Enter your choice here:"))
        if choice == 1:
            a = int(input("Enter your first number here:"))
            b = int(input("Enter your second number here:"))
            result = add(a,b)
            print("Result of addition is :{}\n".format(result))
        elif choice == 2:
            a = int(input("Enter your first number here:"))
            b = int(input("Enter your second number here:"))
            result = sub(a,b)
            print("Result of subtraction is :{}\n".format(result))
        elif choice == 3:
            a = int(input("Enter your first number here:"))
            b = int(input("Enter your second number here:"))
            result = mult(a,b)
            print("Result of multiplication is :{}\n".format(result))
        elif choice == 4:
            try:
                a = int(input("Enter your first number here:"))
                b = int(input("Enter your second number here:"))
                result = div(a,b)
                print("Result of division is :{}\n".format(result))
            except ZeroDivisionError:
                print("Please make sure you don't divide by zero")
        elif choice == 5:
            a = int(input("Enter your first number here:"))
            b = int(input("Enter your second number here:"))
            result = power(a,b)
            print("Result of exponential is :{}\n".format(result))
        elif choice == 6:
            a = int(input("Enter your first number here:"))
            b = int(input("Enter your second number here:"))
            result = root(a)
            print("Result of square root is :{}".format(result))
        else:
            print("Please enter a valid choice\n")
    except ValueError:
        print("Enter valid intergers for the operations to work properly\n")
        if choice == 4:
            print("Please make sure that your second number is not a zero\n")