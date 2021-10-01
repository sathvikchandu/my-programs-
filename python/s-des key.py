
key= input("enter the key : ")        #entering key
l= list(key)
p=[2,4,1,6,3,9,0,8,7,5]        #p10->since it is 0-indexed, i reduced the values by 1 
p8=[5,2,6,3,7,4,9,8]           #p8
l1=[None]*10                    #empty list of size 10
a=0
for i in p:
    l1[a]=l[i]                #arranging the elements as per p10 order
    a+=1
h1=l1[0:5]                    #splitting the matrices
h2=l1[5:10]
b1=h1[0]
h1.pop(0)                      #1 bit shift 
h1.append(b1)
b2=h2[0]
h2.pop(0)
h2.append(b2)

s1_pre=h1+h2                  #merging the matrix 
k1=[None]*8
bo=0
for i in p8:
    k1[bo]=s1_pre[i]         #finally arranging as per p8 pattern 
    bo+=1       
k1="".join(k1)
print ("key k1 is ",k1)     #key k1 is generated



b3=h1[0]
b4= h1[1]                            #performing 2 bit shifts
b5=h2[0]
b6=h2[1]

h1.pop(0)
h1.pop(1)
h1.append(b3)
h1.append(b4)
                                        #2 bit shifting
h2.pop(0)
h2.pop(0)


h2.append(b5)
h2.append(b6)

pre_str2=h1+h2


cont=0
k2=[None]*8
for i in p8:                          #generating the k2 as per p8 matrix
    k2[cont]=pre_str2[i]
    cont+=1
k2="".join(k2)
print("k2 is : ", k2)




