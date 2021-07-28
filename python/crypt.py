
file1 = open("myfile.txt", "w")
L = ["Hello, I am sathvik"]
  

file1.writelines(L)
file1.close()  
  
file1 = open("myfile.txt", "r+")
  
l=file1.read()



l1= list(l)
l2=[]
print(len(l1))
for i in l1:
    o=ord(i)
    l2.append(o)
print(l2)
l3=[]
for i in l1:
    o=ord(i)+4
    l3.append(o)
print(l3)
stri=""
for i in l3:
    op= chr(i)
    stri+=op
print(l)
print(stri)




