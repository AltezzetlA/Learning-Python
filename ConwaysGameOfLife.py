import sys, random, time
#Conway's Game of Life

#set the staring grid size
WIDTH = 30
HEIGHT = 30
grid = []
#define the staring living and dead cells grid
for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if random.randint(0, 10) < 3:
            column.append('██') #append living cell
        else:
            column.append('  ')
    grid.append(column) #append dead cell


def checkNeighboringCells():
    global WIDTH, HEIGHT, grid
    for x in range(WIDTH):    
        for y in range(HEIGHT):
            aliveNeighborCount = 0  
            if x > 0:
                if grid[x - 1][y] == '██': #check neighboring cell to the West
                    aliveNeighborCount += 1
            if x < WIDTH - 1:
                if grid[x + 1][y] == '██': #check neighboring cell to the East
                    aliveNeighborCount += 1
            if y > 0:
                if grid[x][y - 1] == '██': #check neighboring cell North
                        aliveNeighborCount += 1
            if y < HEIGHT - 1:
                if grid[x][y + 1] == '██': #check neighboring cell South
                        aliveNeighborCount += 1
            if x > 0 and y > 0: 
                if grid[x - 1][y - 1] == '██': #check neighboring cell Northwest
                        aliveNeighborCount += 1    
            if x < WIDTH - 1 and y > 0:    
                if grid[x + 1][y - 1] == '██': #check neighboring cell Northeast
                        aliveNeighborCount += 1   
            if x > 0 and y <  HEIGHT -1:   
                if grid[x - 1][y + 1] == '██': #check neighboring cell Southwest
                        aliveNeighborCount += 1  
            if x < WIDTH - 1 and y < HEIGHT -1: 
                if grid[x + 1][y + 1] == '██': #check neighboring cell Southeast
                        aliveNeighborCount += 1  
            if grid[x][y] == '██':
                cellCondition = ['alive', aliveNeighborCount, x, y,] #populate information about the cell
            else: 
                cellCondition = ['dead', aliveNeighborCount, x, y,] #populate information about the cell
            yield cellCondition #output data for each cell


def deadOrAlive(): #generate the next grid
    global grid
    genList = list(checkNeighboringCells()) #compile the data for each cell into one list
    for i in range(len(genList)):
        if genList[i][0] == 'alive' and genList[i][1] != 2 and genList[i][1] != 3: #define conditions for a living cell to die
            grid[genList[i][2]][genList[i][3]] = '  '
        elif genList[i][0] == 'dead' and genList[i][1] == 3: #define condition to revive cell
            grid[genList[i][2]][genList[i][3]] = '██'

def printGrid():
    for x in range(WIDTH - 1):
        for y in range(HEIGHT - 1):
               print(grid[x][y], end='')
        print()
    print("--------------------------------------")


while True:
    printGrid()
    checkNeighboringCells() 
    deadOrAlive() #generate the next grid
    time.sleep(0.5)
