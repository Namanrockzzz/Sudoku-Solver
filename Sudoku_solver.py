from sys import setrecursionlimit
setrecursionlimit=11000

def balance(x,i,j,sudoku,n):
    for col in range(n):
        if sudoku[i][col]==x:
            return False
    for row in range(n):
        if sudoku[row][j]==x:
            return False
    box=Box(i,j,sudoku)
    for b in box:
        if b==x:
            return False
    
    return True

def Box(i,j,sudoku):
    rowS=3*(i//3)
    colS=3*(j//3)
    box=[]
    for row in range(rowS,rowS+3):
        for col in range(colS,colS+3):
                box.append(sudoku[row][col])
    return box

def sudokuSolver(i,j,n,options,sudoku):
    if i>=n:
        return True
    if i<n and j>=n:
        return sudokuSolver(i+1,0,n,options,sudoku)
    if sudoku[i][j]==0:
        for x in options:
            if balance(x,i,j,sudoku,n):
                sudoku[i][j]=x
                isSolved=sudokuSolver(i,j+1,n,options,sudoku)
                if isSolved:
                    return True
                sudoku[i][j]=0

    if sudoku[i][j]==0:
        return False
    return sudokuSolver(i,j+1,n,options,sudoku)


sudoku=[[int(i) for i in input().split()] for j in range(9)]
sudokuSolved=sudokuSolver(0,0,9,[1,2,3,4,5,6,7,8,9],sudoku)
print()
print()

if sudokuSolved:
    for i in range(9):
        for j in range(9):
            print(sudoku[i][j],end=" ")
        print()
    print("true")
else:
    print("false")