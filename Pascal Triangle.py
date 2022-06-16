# https://www.codingninjas.com/codestudio/problems/pascal-s-triangle_1089580?topList=striver-sde-sheet-problems

# https://leetcode.com/problems/pascals-triangle/

def printPascal(n:int):
    # Write your code here.
    # Return a list of lists.
    pascal = [[1], [1,1]]
    
    if n == 1:
        return [[1]]
    elif n == 2:
        return pascal
    else:
        for _ in range(n-2):
            tmp = [1]
            for j in range(0, len(pascal[-1])-1):
                tmp.append(pascal[-1][j] + pascal[-1][j+1])
            tmp.append(1)
            pascal.append(tmp)
    return pascal

"""
def printPascal(n:int):
    # Write your code here.
    # Return a list of lists.
    pascal = [[0 for _ in range(n)] for _ in range(n)]

    if n == 1:
        return [[1]]
        
    pascal[0][0] = pascal[1][0] = pascal[1][1] = 1
    for i in range(2, n):
        for j in range(n):
            if j == 0 or j == i+1:
                pascal[i][j] = 1
            else:
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
              
    for i in range(n):
       for j in range(n):
           if pascal[i][j] != 0:
               print(pascal[i][j], end=" ")
       print(" ")
"""