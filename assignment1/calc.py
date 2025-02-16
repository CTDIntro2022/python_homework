
# Task 2
num1 = int(input("First number:"))
num2 = int(input("Second number:"))
addUp = num1 + num2
print (f"Addition: {addUp}")
print (f"Subtraction: {num2 - num1}")
print (f"Multiplication: {num2 * num1}")
outDiv = 0
if (num1 == 0):
    outDiv = "Can't divide by zero"
else:
    outDiv = num2/num1
    
print (f"Division: {outDiv}")