from collections import defaultdict

#print the common sum and the matrix
def printMatrix(matrix):
    global count_solution
    count_solution+=1
    print("solution",count_solution," :")
    print("common sum is ",sum(matrix[0]))
    print("[")
    for row in range(3):
        print(" [", end="")
        for col in range(3):
            if col!=2:
                print(matrix[row][col],end=", ")
            else:
                print(matrix[row][col],end="]\n")
    print("]")

def backtrack(arr, used, matrix, positions, pos_idx, common_sum=0):
    '''
        :param arr: list of numbers to be filled in the matrix
        :param used: indicate whether a number is used. used[idx] = True if arr[idx] is used
        :param matrix: the matrix to be filled
        :param positions: filling order in list, each position is a tuple (row,col)
        :param pos_idx: indicate current position to be fixed
        :param common_sum: common sum of each row/column/diagonal
    '''
    #All positions are filled
    if pos_idx == len(positions):
        printMatrix(matrix)
        return

    #parse the position to be filled
    r, c = positions[pos_idx]
    #fill the position with unused numbers
    for i, val in enumerate(arr):
        if not used[i]:
            # Place val here
            matrix[r][c] = val
            used[i] = True

            # Early pruning: If we have enough info to check partial sums, do it here.
            # has filled the diagonal line from upper left to lower right
            if pos_idx == 2:
                # calculate the sum of the diagonal line from upper left to lower right
                common_sum = sum([matrix[0][0], matrix[1][1], matrix[2][2]])

            # has filled the diagonal line from upper right to lower left
            elif pos_idx == 4:
                # check sum of diagonals
                if common_sum != sum([matrix[0][2], matrix[1][1], matrix[2][0]]): #not equal, prune this branch
                    #reset used and matrix
                    used[i] = False
                    matrix[r][c] = 0
                    continue # skip this branch

            #has filled the up edge
            elif pos_idx == 5:
                #check sum of the first row
                if common_sum != sum(matrix[0]):
                    #reset used and matrix
                    used[i] = False
                    matrix[r][c] = 0
                    continue

            #has filled the left edge
            elif pos_idx == 6:
                #check sum of the first column
                if common_sum != sum(matrix[local_r][0] for local_r in range(3)):
                    #reset used and matrix
                    used[i] = False
                    matrix[r][c] = 0
                    continue

            #has filled the right edge
            elif pos_idx == 7:
                #check sum of the 3rd column and the 2nd row
                if (common_sum != sum(matrix[local_r][2] for local_r in range(3))) or (common_sum != sum(matrix[1])):
                    #reset used and matrix
                    used[i] = False
                    matrix[r][c] = 0
                    continue

            #has filled the bottom edge
            elif pos_idx == 8:
                #check sum of the 3rd row and the 2nd column
                if (common_sum != sum(matrix[2])) or (common_sum != sum(matrix[local_r][1] for local_r in range(3))):
                    #reset used and matrix
                    used[i] = False
                    matrix[r][c] = 0
                    continue

            backtrack(arr, used, matrix, positions, pos_idx+1,common_sum)
            # Backtrack
            used[i] = False
            matrix[r][c] = 0

# Main logic
arr = [1,2,3,4,5,6,7,8,9]
used = [False]*len(arr)
matrix = [[0]*3 for _ in range(3)]
count_solution = 0 #count of solutions

# Define filling order: center -> corners (diagonals) -> edges
positions = [
    (1,1),       # center
    (0,0), (2,2), (0,2), (2,0),  # diagonals
    (0,1), (1,0), (1,2), (2,1)   # edges
]

backtrack(arr, used, matrix, positions, 0)