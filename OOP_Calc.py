# Jake Prisby
# 3/4/2021
# Simple OOP Calculator
# Link to problem: https://edabit.com/challenge/ta8GBizBNbRGo5iC6

# Calculator Object
class Calculator():

    # Desc.: Add the two terms
    # Input: Two Integers
    # Output: The sum of the two integers
    def add( self, num1, num2 ):
        return num1 + num2

    # Desc.: Subtract num2 from num1
    # Input: Two Integers
    # Output: The difference of the two integers
    def subtract( self, num1, num2 ):
        return num1 - num2
    
    # Desc.: Multiply the two terms
    # Input: Two Integers
    # Output: The product of the two numbers
    def multiply( self, num1, num2 ):
        return num1 * num2
    
    # Desc.: Divide the two numbers
    # Input: Two numbers
    # Ouput: The quotient of the two numbers
    def divide( self, num1, num2 ):
        return num1 / num2


calc = Calculator() # Create Calculator Object
cont = True # Boolean used to end loop

while( cont == True ):
    # Print out User Interface to console
    print("1. --> Add")
    print("2. --> Subtract")
    print("3. --> Multiply")
    print("4. --> Divide")
    print("5. --> Exit")

    # Make calculation based on user input
    try:
        num = int(input())

        if( num == 5 ):
            # Here the user wants to end the application, end loop
            cont = False
        elif ( num > 0 and num < 5) :
            # Here the user wants to make a calculation, get input
            print("Enter number 1: ")
            num1 = int(input())
            print("Enter number 2: ")
            num2 = int(input())

            # Make calculation based on the numbers the user gave
            if ( num == 1 ):
                print("= " + str(calc.add(num1, num2)))
            elif ( num == 2 ):
                print("= " + str(calc.subtract(num1, num2)))
            elif ( num == 3 ):
                print("= " + str(calc.multiply(num1, num2)))
            elif ( num == 4):
                print("= " + str(calc.divide(num1, num2)))

        else:
            # Here the user entered an invalid input
            print("ERROR: Invalid input, enter a number that corresponds to a process that is displayed")
    except ValueError:
        print("ERROR: Invalid input, non-number input recieved when expecting number input")
