
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

# Task 5
try:
    float1 = float (input ("Enter numerator:"))
    float2 = float (input ("Enter denominator:"))
    divResult = float1/float2
    print (f"Division: {divResult}")
except ZeroDivisionError:
   print("You cannot divide a value with zero")
except ValueError:
    print("one of two inputs not a float")
except:
   print("Something else went wrong")
