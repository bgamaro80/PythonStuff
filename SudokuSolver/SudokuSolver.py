from glob import glob
import numpy as np
from colorama import Fore
from colorama import Style
import time
import os

initialState = np.array(
    (0,4,0,0,0,0,9,0,0,
     8,2,5,0,9,4,0,6,0,
     0,0,0,2,0,0,4,0,0,
     0,6,0,0,0,1,0,0,0,
     4,0,8,0,7,2,0,9,0,
     0,9,3,5,4,0,0,0,0,
     0,7,0,0,0,9,3,8,0,
     0,0,4,0,3,8,0,0,5,
     0,0,0,7,2,0,0,0,0
     ), dtype=np.uint8)
    
board = np.array(initialState, copy=True)
foundSolution = False
iterations = 0

cell1 = np.array((0,1,2,9,10,11,18,19,20), dtype=np.uint8)
cell2 = np.array((3,4,5,12,13,14,21,22,23), dtype=np.uint8)
cell3 = np.array((6,7,8,15,16,17,24,25,26), dtype=np.uint8)

cell4 = np.array((27,28,29,36,37,38,45,46,47), dtype=np.uint8)
cell5 = np.array((30,31,32,39,40,41,48,49,50), dtype=np.uint8)
cell6 = np.array((33,34,35,42,43,44,51,52,53), dtype=np.uint8)

cell7 = np.array((54,55,56,63,64,65,72,73,74), dtype=np.uint8)
cell8 = np.array((57,58,59,66,67,68,75,76,77), dtype=np.uint8)
cell9 = np.array((60,61,62,69,70,71,78,79,80), dtype=np.uint8)

def printBoard():
    print("-------------------------")
    printBoardLine(0)
    printBoardLine(1)
    printBoardLine(2)
    print("-------------------------")
    printBoardLine(3)
    printBoardLine(4)
    printBoardLine(5)
    print("-------------------------")
    printBoardLine(6)
    printBoardLine(7)
    printBoardLine(8)
    print("-------------------------")

def printBoardLine(row):
    rowIndex = row * 9
    for i in range(rowIndex, rowIndex + 9, 1):
        if i % 3 == 0:
            print("| ", end='')
        
        if initialState[i] != 0:
            print(f"{Fore.MAGENTA}{board[i]}{Style.RESET_ALL} ", end='')
        elif board[i] == 0:
            print("  ", end='')
        else:
            print(f"{board[i]} ", end='')
    
    print("|")

def isValidNumer(step):
    global iterations
    iterations += 1
    #row
    firstRowStep = step - (step % 9)
    rowValues = board[firstRowStep:firstRowStep+9]
    filter = rowValues > 0
    rowValues = rowValues[filter]
    setValues = set(rowValues)
    if rowValues.size != len(setValues):
        return False
    
    #column
    firstRowStep = step % 9
    rowValues = np.zeros(9, dtype=np.uint8)
    for i in range(0, 9, 1):
        rowValues[i] = board[firstRowStep+(i*9)]
    filter = rowValues > 0
    rowValues = rowValues[filter]
    setValues = set(rowValues)
    if rowValues.size != len(setValues):
        return False
    
    #cell
    if step in cell1:
        stepIndexes = cell1
    elif step in cell2:
        stepIndexes = cell2
    elif step in cell3:
        stepIndexes = cell3
    elif step in cell4:
        stepIndexes = cell4
    elif step in cell5:
        stepIndexes = cell5
    elif step in cell6:
        stepIndexes = cell6
    elif step in cell7:
        stepIndexes = cell7
    elif step in cell8:
        stepIndexes = cell8
    elif step in cell9:
        stepIndexes = cell9
    
    rowValues = np.zeros(9, dtype=np.uint8)
    for i, stepIndex in enumerate(stepIndexes):
        rowValues[i] = board[stepIndex]
    
    filter = rowValues > 0
    rowValues = rowValues[filter]
    setValues = set(rowValues)
    if rowValues.size != len(setValues):
        return False
    
    return True

def solveSudoku(step):
    global foundSolution
    
    if step >= 9*9:
        return
    
    if initialState[step] > 0:
        solveSudoku(step + 1)
        return
    
    for value in range(1, 10, 1):
        if foundSolution:
            return
        
        board[step] = value
        
        # os.system('cls' if os.name == 'nt' else 'clear')
        # printBoard()
        # time.sleep(0.1)
        
        if isValidNumer(step):
            if step == 80:
                foundSolution = True
                
            solveSudoku(step + 1)
    
    if not foundSolution and initialState[step] == 0:
        board[step] = 0

def main():
    global foundSolution
    solveSudoku(0)
    printBoard()
    
    if foundSolution:
        print("Solved!")
    
    print(f"{iterations} iteraciones")

if __name__ == "__main__":
    main()