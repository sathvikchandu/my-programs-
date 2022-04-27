key=[3,4,5,6,7,8,9,1,13,32]
n=8

key_list = [key[i:i + n] for i in range(0, len(key), n)] 
print(key_list)