'''
arr has 12 integers
matrix is 3x3
fill the matrix with the integers in arr to make it a magic square
magic square: sum of all rows, columns, and diagonals are equal
'''
from collections import defaultdict
import copy

#find all possible magic squares
def backtrack(arr,val_idx_map,matrix,selected,row,col,cur_sum):
    '''
    :param arr: arr of 12 intergers
    :param val_idx_map: A map from a value to its possible indices in arr. This is helpful if there are duplicate values in arr. {value:[index1,index2,...]}
    :param matrix: matrix to be filled
    :param selected: selected[idx] is True if arr[idx] is already in the matrix
    :param row and col:
        current position in the matrix to be filled.
        row=col=0 means the top left entry (matrix[0][0]) is to be filled
        row=0 and col=1 means the top middle entry(matrix[0][1]) is to be filled while matrix[0][0] are already filled
        when col=2, we move to the next row by backtrack(arr, val_idx_map, matrix, selected, row + 1, 0, cur_sum)
        when row=2 and col=0, we have filled the first two rows, and we directly deduce the third row by the column sum. And then check the sum of the 3rd row and two diagonals, then print the matrix if it is a magic square
    :param cur_sum: sum of the first row
    :return:
    '''
    #pre
    #has filled with the first row, calculate the sum of the first row
    if row==1 and col==0: #sum the fist low
        cur_sum=sum(matrix[row-1])

    #has filled with the second row, fill the third row by first two rows' sum, and check the diagonals
    if row==2 and col==0:
        if sum(matrix[row-1])!=cur_sum: #second row's sum != first row's sum
            return
        else: #first two rows' sum are equivalent, now fill the third row
            pre_matrix=copy.deepcopy(matrix)
            pre_selected=copy.deepcopy(selected)
            for col_idx in range(3):
                entry=cur_sum-matrix[0][col_idx]-matrix[1][col_idx]
                if entry not in arr:
                    #reset selected and matrix
                    selected[:]=pre_selected
                    matrix[:]=pre_matrix
                    return
                else: #entry is in arr
                    #check selected
                    for idx in val_idx_map[entry]:
                        if not selected[idx]: #entry is not selected
                            selected[idx]=True
                            matrix[row][col_idx]=entry
                            break
                    else: #no available unselected entry
                        # reset selected and matrix
                        selected[:] = pre_selected
                        matrix[:] = pre_matrix
                        return
            #no return in advance -> all entries in the third row are filled
            if cur_sum==sum(matrix[2]): #all rows' sum are equal
                #check diagonals (because rows and columns are already checked)
                if matrix[0][0]+matrix[1][1]+matrix[2][2]==cur_sum and matrix[0][2]+matrix[1][1]+matrix[2][0]==cur_sum: #is a magic square
                    printMatrix(matrix)
            #Regardless magic or not : reset selected and matrix by clear the 3rd row and then return
            selected[:] = pre_selected
            matrix[:] = pre_matrix
            return
    #in
    for idx in range(12): #try all unselected entries in the arr
        if not selected[idx]:
            selected[idx]=True
            matrix[row][col]=arr[idx]
            if col==2: #move to the next row
                backtrack(arr, val_idx_map, matrix, selected, row + 1, 0, cur_sum)
            else: #move to the next column
                backtrack(arr,val_idx_map,matrix,selected,row,col+1,cur_sum)
            #come back and reset the selected and matrix
            selected[idx]=False
            matrix[row][col]=0

    #post
    #has tried all potentials at matrix[row][col], return
    return

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

arr=[1,6,8,5,3,7,4,9,2,10,11,12]
'''
[
    [8,1,6]
    [3,5,7]
    [4,9,2]
]
is a magic square
'''
selected = [False]*12
matrix = [[0]*3 for _ in range(3)]
val_idx_map= defaultdict(list)
for idx,val in enumerate(arr):
    val_idx_map[val].append(idx)
count_solution=0
backtrack(arr,val_idx_map,matrix,selected,0,0,0)
