def matrixGen(key):     #defined a finction which takes key as a parameter
    matrix = []         #created an empty list
    for alpha in key.upper():       #for loop to iterate through the key
        if alpha not in matrix:     #if the letter is not in the matrix
            matrix.append(alpha)    #append the letter to the matrix
    alphabets = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    for alpha in alphabets:         #for loop to iterate through the alphabets string
        if alpha not in matrix :    #if the letter is not in the matrix(i.e. not in the key)
            matrix.append(alpha)    #append the letter to the matrix
    key_matrix = [matrix[0:5], matrix[5:10], matrix[10:15], matrix[15:20], matrix[20:25]]   #cconverting the list into a matrix of 5 rows and 5 columns
    return key_matrix   #returning the matrix

 #main function
key = input("Enter the key: ")   #taking the key as input   
print(matrixGen(key))           #printing the matrix