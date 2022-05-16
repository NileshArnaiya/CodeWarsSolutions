def getIndex(matrix):
    listIndex = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            # print(matrix[i][j])
            if matrix[i][j] == 0:
                # print("J is ", j)
                listIndex.append([i,j])
    return listIndex
    
def solution(matrix):

    if len(matrix) > 1:
        myList = getIndex(matrix)
        newList = []
        for i,j in myList:
            #print(i,j)
            matrix[i][j] == 0
            if i < 2:
                newList.append([i+1, j])
        # print("Length ", len(newList))
        # print("MyList is still ", myList)
        # print("NewList is ", newList)
        # print("MixedList ", newList + myList)
        
        for i,j in newList+myList:
            print(i,j)
            # matrix[i][j] == 0
        print("Matrix is ", matrix)
        oknew = [list(t) for t in set(tuple(element) for element in newList+myList)]
        oknew = sorted(oknew)
        # print(oknew)
        for i in oknew:
            matrix[i[0]][i[1]] = 0            
        # print("I is ",matrix[i[0]][i[1]] == 0, " j is ", i[1])        
        print("Matrix is ", matrix)
        flatten_list = [j for sub in matrix for j in sub]
        return sum(flatten_list)
    elif matrix[0][0] == 0:
        return 0
    else:
        return matrix[0][0]
        
    # for i in range(0, len(matrix)):
    #     for j in range(0, len(matrix[i])):
    #         for k,l in newList:
    #             matrix[k][l] == 0
    # print("matrix " , matrix)
    