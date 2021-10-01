import numpy as np  #importing numpy module for list operations

def table_shift(array, table_array):   #table_shift function to permutate according the permutation table
    array_shifted = np.zeros(table_array.shape[0], dtype='int')  #initializing array_shifted with zeros
    for index, value in enumerate(table_array): array_shifted[index] = array[value - 1]  #shifting the array according to the table
    return array_shifted     #returning the shifted array

def array_split(array):    #function to split the array into two halves
    left_split = array[:int(len(array) / 2)]   #slicing the list upto the middle and considering the left half
    right_split = array[int(len(array) / 2):]  #slicing the list from the middle and considering the right half
    return left_split, right_split   #returning the left and right split

def shifting_LtoR(array):   #function to shift the array from left to right
    temp = array[0]    #storing the first element of the array
    for index in range(1, len(array)): array[index - 1] = array[index]  #shifting the array from left to right
    array[len(array) - 1] = temp  #replacing the last element of the array with the first element
    return array 

table_p_10 = np.array([3, 5, 2, 7, 4, 10, 1, 9, 8, 6])    #permutation table for P10
table_p_08 = np.array([6, 3, 7, 4, 8, 5, 10, 9])   #permutation table for P8

ke = input("enter the key : ")#key to be used for encryption
key = list(ke)
print("the keys k1 and k2 are :")
def split_and_merge(key):     #function to split the key into two halves and merge them
    left_split, right_split = array_split(key)    #splitting the key into two halves
    return np.concatenate((shifting_LtoR(left_split), shifting_LtoR(right_split)))   #merging the two halves

def key_generation_1(key, table):    #function to generate the key for round 1
    k = table_shift(key, table)   #shifting the key according to the permutation table p10
    key_merge = split_and_merge(k)    #merging the two halves
    return table_shift(key_merge, table)   #shifting the key according to the permutation table p10

def key_generation_2(key, table): return split_and_merge(key)    #function to generate the key for round 2

key_1 = key_generation_1(key, table_p_10)     #generating the key for round 1
print("".join([str(elem) for elem in key_1]))  #1000111010    #printing the key for round 1

key_2 = key_generation_2(key_1, table_p_08)     #generating the key for round 2
print("".join([str(elem) for elem in key_2]))  #0001110101    #printing the key for round 2