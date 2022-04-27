key=[9,10,11,12]
n=8

key_list = [key[i:i + 3] for i in range(0, len(key), n)]
print(key_list)