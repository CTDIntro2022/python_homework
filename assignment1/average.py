#Task 4

def calculate_average (listOfNums):
    scoreSum = 0
    scoreCount = 0
    for score in listOfNums:
        scoreSum += float(score)
        scoreCount += 1

    avgScore = scoreSum/scoreCount
    print ("Average Score: ", avgScore)

scoreList = input ("Enter mutliple scores seperated by comma:")
scoreRay = scoreList.split(",")

# check input
for score in scoreRay:
    try:
        tempFloat = float (score)
    except:
        print (f"{score} cannot be converted to float.")
        exit()

# IF we get here are values can be converted to float
calculate_average (scoreRay)
