import math
modulo_p=int(input("Enter modulo p: "))           
primitive_p=int(input("Enter primitive root of p: "))   
secret_1=int(input("Enter secret number 1: "))         
secret_2=int(input("Enter secret number 2: "))

a=math.pow(primitive_p,secret_1)%modulo_p   #a=g^a mod p

b=math.pow(primitive_p,secret_2)%modulo_p  #b=g^b mod p

se_a=math.pow(b,secret_1)%modulo_p         #se_a=b^a mod p

se_b=math.pow(a,secret_2)%modulo_p       #se_b=a^b mod p

if se_a==se_b:
    print("two parties can communicate with each other using shared scret no. ",int(se_a) )
else:
    print("Two parties cannot communicate")