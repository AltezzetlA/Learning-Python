values = []

while True: #take user inputs. Verify that the inputs are integers. Input is finished when the user types 'finished'
    userInput = input('Please enter a value, or type "finished" to finish: ') 
    if userInput.lower() == 'finished':
        break
    else:
        try:
            values += [int(userInput)]
            continue
        except ValueError:
            print('Please only input numerical values or "finished".')
            continue
   
    
def average():
    try:
        numerator = 0
        for i in range(len(values)): #derrive the numerator by adding all the numbers in the values list
            numerator += values[i]
        avg = numerator / len(values) #divide the numerator by the denominator to derrive the average
        return avg
    except ZeroDivisionError:
        print('You must enter a number. Please try again.')
    
#print(f'The average of the numbers input is : {average()}')


def mode():
    occuranceCount = [] #create a list to log the number of occurances for each number
    valuesMode = values.copy()
    for i in range(len(valuesMode)):
        sameNumberCount = 0 #define a counter for the number of occurances for each number
        integer = valuesMode[i]
        for j in range(len(valuesMode)): 
            if valuesMode[j] == integer and integer != None: 
                sameNumberCount += 1 #increase the number of occurances
                valuesMode[j] = None
        occuranceCount += [[sameNumberCount, integer]]
    
    maximumCompare = 0
    for i in range(len(occuranceCount)):
        if occuranceCount[i][0] > maximumCompare:
            modeList = occuranceCount[i]
            maximumCompare = occuranceCount[i][0]
        elif occuranceCount[i][0] == maximumCompare:
            modeList += occuranceCount[i]

    print('The mode(s) of the entered numbers are ', end='')
    for i in range(len(modeList)):
        print(f'{modeList[2 * i]},')
    print(f'which occur(s) {modeList[0]} times')

        


print(mode())
