import time
class Emporia: 
    def __init__(self):
        self.matrix = []
        self.visitedMatrix = []
        self.rows = 0
        self.columns = 0
        self.startX = 0 
        self.startY = 0
        self.endX = 0
        self.endY = 0
        self.numOfObstacle = 0
        self.numOfUnvisited = 2
        self.totalPath = 0
    
    def handleInput(self):
        matrixDepth = input().split(" ")
        self.rows = int(matrixDepth[0])
        self.columns = int(matrixDepth[-1])
        self.matrix = [list(map(int,input().split())) for i in range(self.rows)]         
        
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                element = self.matrix[i][j]
                row.append(element)
                if element == 2:
                    self.startX, self.startY = i, j
                    
                elif element == 3: 
                    self.endX, self.endY = i, j  
                elif element == 1:
                    self.numOfObstacle += 1
                elif element == 0: 
                    self.numOfUnvisited += 1
            self.visitedMatrix.append(row)

    def checkIndex(self,row, column): 
        if row < self.rows and row >= 0 and column < self.columns and column >= 0:
            travelPoints = [0,2,3]
            if self.visitedMatrix[row][column] in travelPoints:
                return True
        return False
    
    def printMatrix(self):
        for i in range(self.rows):
            for j in range(self.columns):
                print(self.matrix[i][j], end=" ")
            print()

    def isTravelAll(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.visitedMatrix[i][j] == 0:
                    return False 
        return True

    def travelPath(self, row, column):
        if row == self.endX and column == self.endY and self.isTravelAll():
            self.totalPath += 1
            
        if self.visitedMatrix[row][column] not in [2, 3]:
            self.visitedMatrix[row][column] = 1     # this place is visited
        
        if self.checkIndex(row + 1, column):
            self.travelPath(row + 1, column)

        if self.checkIndex(row - 1, column):
            self.travelPath(row - 1, column)

        if self.checkIndex(row, column + 1):
            self.travelPath(row, column + 1)

        if self.checkIndex(row, column - 1):
            self.travelPath(row, column - 1)
        
        if self.visitedMatrix[row][column] not in [2, 3]:
            self.visitedMatrix[row][column] = 0         # for backtracking
            
        return
    
    def solution(self):
        self.handleInput()
        self.travelPath(self.startX, self.startY)
        
        print(self.totalPath)

emp = Emporia()

emp.solution()


# print(startX, startY, endX, endY, numOfObstacle, totalPath)