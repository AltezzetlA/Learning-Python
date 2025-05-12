from random import *
import random, sys, os, math
winCount = 0
loseCount = 0
drawCount = 0

#establish gameplay loop
while True:
    PlayerStr = input('Please enter rock, paper, scissors, or exit: ').lower()
    #Convert player input string into numerical value for comparison
    if PlayerStr == 'rock':
        PlayerNum = 1 #1 = Rock
    elif PlayerStr == 'paper':
        PlayerNum = 2 #2 = Paper
    elif PlayerStr == 'scissors':
        PlayerNum = 3 #3 = Scissors
    elif PlayerStr == 'exit':
        break
    else:
        print('Invalid input.')

    #generate random number for computer
    ComputerNum = random.randint(1, 3)

    #assign string value to computer number
    if ComputerNum == 1:
        ComputerStr = 'rock'
    elif ComputerNum == 2:
        ComputerStr = 'paper'
    elif ComputerNum == 3:
        ComputerStr = 'scissors'
    #establish win condition
    if PlayerNum == ComputerNum:
        drawCount += 1
    elif PlayerNum == 1 and ComputerNum == 3:
        winCount += 1
    elif ComputerNum == PlayerNum - 1: #PlayerNum > ComputerNum:
        winCount += 1
    else:
        loseCount = loseCount + 1
    print('Computer: ' + ComputerStr + ' You: ' + PlayerStr)
    print('WIN: ' + str(winCount) + ' LOSE: ' + str(loseCount) + ' DRAW: ' + str(drawCount))
print('Thank you for playing!')
