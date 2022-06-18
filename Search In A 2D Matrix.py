# https://www.codingninjas.com/codestudio/problems/search-in-a-2d-matrix_980531?topList=striver-sde-sheet-problems&leftPanelTab=1

def findTargetInMatrix(mat, m, n, target):
    
    i, j = 0, n-1
    while i < m and j >= 0:
        if mat[i][j] == target:
            return True
        elif mat[i][j] < target:
            i += 1
        elif mat[i][j] > target:
            j -= 1
            
    return False