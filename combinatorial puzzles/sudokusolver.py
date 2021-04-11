import sys

def isValid1(out):
    return True

def auxSudokuSolver1(r, c, inp, out):
    if(r == 9):
        if(isValid1(out)):
            print(out)
        return
    if(inp[r][c] != 0):
        auxSudokuSolver1(r+1 if c==8 else r, (c+1)%9, inp, out)
    else:
        for d in range(1, 10):
            out[r][c] = d
            auxSudokuSolver1(r+1 if c==8 else r, (c+1)%9, inp, out)

def sudokuSolver1(inp):
    out = [ [0]*9 for i in range(9)]
    for i in range(9):
        for j in range(9):
            out[i][j] = inp[i][j]
    auxSudokuSolver1(0, 0, inp, out)
#--------------------------------------------------------------
def isValid2(r, c, d, out):
    #row check
    for j in range(9):
        if(out[r][j] == d):
            return  False
    #column check
    for i in range(9):
        if(out[i][c] == d):
            return  False
    #subgrid check
    sr = r // 3 * 3
    sc = c // 3 * 3
    for i in range(3):
        for j in range(3):
            if(out[sr+i][sc+j] == d):
                return False
    return True

def auxSudokuSolver2(r, c, inp, out):
    if(r == 9):
        print(out)
        return
    if(inp[r][c] != 0):
        auxSudokuSolver2(r+1 if c==8 else r, (c+1)%9, inp, out)
    else:
        for d in range(1, 10):
            if(isValid2(r, c, d, out)):
                out[r][c] = d
                auxSudokuSolver2(r+1 if c==8 else r, (c+1)%9, inp, out)
        out[r][c] = 0

def sudokuSolver2(inp):
    out = [ [0]*9 for i in range(9)]
    for i in range(9):
        for j in range(9):
            out[i][j] = inp[i][j]
    auxSudokuSolver2(0, 0, inp, out)
#--------------------------------------------------------------
    
def main():
    #inp = [ [0]*9 for i in range(9)]
    inp = [ 
				[ 4, 0, 0, 0, 0, 0, 0, 0, 0 ],
				[ 0, 0, 0, 0, 0, 9, 0, 0, 0 ], 
				[ 0, 0, 0, 0, 0, 0, 7, 8, 5 ],
				[ 0, 0, 7, 0, 4, 8, 0, 5, 0 ], 
				[ 0, 0, 1, 3, 0, 0, 0, 0, 0 ],
				[ 0, 0, 6, 0, 7, 0, 0, 0, 0 ], 
				[ 8, 6, 0, 0, 0, 0, 9, 0, 3 ],
				[ 7, 0, 0, 0, 0, 5, 0, 6, 2 ], 
				[ 0, 0, 3, 7, 0, 0, 0, 0, 0 ] 
			]
    print(inp)
    sudokuSolver2(inp)
    
if __name__=="__main__":
    main()
