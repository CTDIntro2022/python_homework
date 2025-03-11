# Task 3

score = int(input("Single grade:"))
grade = "F"

if (score > 90):
    grade = "A"
elif (score > 80):
    grade = "B"
elif (score > 70):
    grade = "C"
elif (score > 60):
    grade = "D"
else:
    grade = "F"         # Redundant with initial value but good for clarity

print (f"Grade is {grade}")

scoreRay = []
while True:
    try:
        line = input("Enter score, CTRL-Z to finish:")
    except EOFError:
        break
    scoreRay.append(line)

scoreSum = 0
scoreCount = 0
for score in scoreRay:
    scoreSum += float(score)
    scoreCount += 1

avgScore = scoreSum/scoreCount
print ("Average Score: ", avgScore)
