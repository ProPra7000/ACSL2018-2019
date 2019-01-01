"""
Name: Prahalad Ramakrishnan
School: Chantilly High School
Division: Senior
"""
#repeats code to ask for input 5 times
for i in range(5):

    #Asks for input
    userinput = str(input("Enter your input: "))

    #initialization of variables
    num = ""
    arrayNum = ""
    array = []
    repeats = 0
    numOfRepeats = 0
    total = 0

    #seperates user input the number to be worked/added with
    for i in userinput:
        if (i != " "):
            num += i
        elif (i == " "):
            break

    #seperates user input to find the length of each non-overlapping number
    length = int(userinput[len(userinput) - 1])

    #finds the amount of times that the code has to find non-overlapping numbers
    if (len(num) % length == 0):
        numOfRepeats = len(num)/length
    else:
        while (len(num) % length != 0):
            num += "0"
        numOfRepeats = len(num)/length
    numOfRepeats = int(numOfRepeats)

    #adds the non-overlapping pieces of numbers to an array
    for a in range(0, numOfRepeats):
        for b in range(length*repeats, length*(repeats + 1)):
            arrayNum += num[b]
        arrayNum = int(arrayNum)
        array.append(int(arrayNum))
        arrayNum = ""
        repeats += 1

    #adds the numbers together
    total = sum(array)
    
    #outputs the number
    print (total)
