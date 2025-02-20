# Assignment 2
# Put code here

# Task 1
def perform_operations (a, b):
    print (f"Operations on {a} and {b}:")
    print (f"  Multiplication: {a*b}")
    print (f"  Addition: {a + b}")
    print (f"  Subtraction: {a - b}")

    # Division - check for 0
    if not b:
        print ("  Division: Can't divide by 0")
    else:
        print (f"  Division: {a/b}")
    
    # Floor division
    if not b:
        print ("  Floor division: Can't floor divide by 0")
    else:
        print (f"  Floor division: {a//b}")
    
    # Modulos
    if not b:
        print ("  Modulus 0 is not allowd")
    else:
        print (f"  Modulus: {a % b}")
    
    # Exponentiation
    print ((f"  Exponentiation: {a**b}"))

perform_operations (10,3)

