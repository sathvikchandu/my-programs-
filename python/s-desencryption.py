# function for permutation tacking p-box,binary string to be permuted and length of binary string as input
# and returning permuted binary string as a output
def permute(p,s,l):
    ns=''                  
    for i in range(l):
        ns += s[p[i] - 1]
    return ns


def keygenerator(key):
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
    #key k1 is generated



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
    return k1,k2


# function for left circular shift operation tackin binary string and its length as input
# and returning shifted binary string as a output
def lcs(ss,n):
    rlcs=''                  
    for i in range(len(ss)):
        rlcs+=ss[(n+i)%5]
    return rlcs

#function for diving string tackin binary string and and divider number as input and
#returning splited binary strings
def spliter(s,d):
    split1=s[0:d]
    split2=s[d:]
    return(split1,split2)

#key generator function
def keygenerator(p10,p8,key):
    keyp = permute(p10, key, 10)

    ls1, ls2 = spliter(keyp, 5)

    ls1 = lcs(ls1, 1)
    ls2 = lcs(ls2, 1)
    ls = ls1 + ls2
    k1 = permute(p8, ls, 8)

    ls1 = lcs(ls1, 2)
    ls2 = lcs(ls2, 2)
    ls = ls1 + ls2
    k2 = permute(p8, ls, 8)

    return(k1,k2)

#function for doing xor operation between two strings and tacking two binary strings and and it's length as input and
#returning binary string output of two strings
def doxor(s1,s2,l):
    c = ''                          
    for i in range(l):
        c = c + str(int(s1[i]) ^ int(s2[i]))
    return c

#function for converting binary string into integer number
def stoi(sdata):
    return int(sdata,2)

#function for returning indexes for s-boxes
def giveindex(data):
    r=stoi(data[0]+data[3])
    c=stoi(data[1]+data[2])
    return (r,c)


#START OF SDES ENCRYPTION ALGORITHM
def sdes_encryption(plaintext,key,ip,ep,s1,s2,p4,p10,p8):
    ipinv = []
    for i in range(8):  # Finding inverse of ip
        ipinv.append(ip.index(i + 1) + 1)

    key1, key2 = keygenerator(p10, p8, key)
    plaintextip = permute(ip, plaintext, 8)

    l0, r0 = spliter(plaintextip, 4)

    # Round 1
    u_r0 = permute(ep, r0, 8)  # Expansion Permutation
    xorout = doxor(u_r0, key1, 8)  # XOR operation with key
    sbx1, sbx2 = spliter(xorout, 4)  # Spliting of output of xor operation
    r1r1, r1c1 = giveindex(sbx1)  # Getting index for sbox s1 & s2 from splited string
    r1r2, r1c2 = giveindex(sbx2)
    u_r0 = format(s1[r1r1][r1c1],'b') + format(s2[r1r2][r1c2],'b')  # Getting according data from s-boxes converted into binary string
    u_r0 = permute(p4, u_r0, 4)  # Last 4 bit permutation
    # end of Round 1

    r1 = doxor(l0, u_r0, 4)  # Swaping for Round-2
    l1 = r0

    # Round 2
    u_r1 = permute(ep, r1, 8)  # Expansion Permutation
    xorout = doxor(u_r1, key2, 8)  # XOR operation with key
    sbx1, sbx2 = spliter(xorout, 4)  # Spliting of output of xor operation
    r2r1, r2c1 = giveindex(sbx1)  # Getting index for sbox s1 & s2 from splited string
    r2r2, r2c2 = giveindex(sbx2)
    u_r1 = format(s1[r2r1][r2c1],'b') + format(s2[r2r2][r2c2],'b')  # Getting according data from s-boxes converted into binary string
    u_r1 = permute(p4, u_r1, 4)  # Last 4 bit permutation
    u_r1 = doxor(u_r1, l1, 4)
    # end of Round 2

    last = u_r1 + r1
    ciphertext = permute(ipinv, last, 8)  # Permutation with inverse of initial permutation(ip)
    return ciphertext
#END OF SDES ENCRYPTION ALGORITHM

#START OF SDES DECRYPTION ALGORITHM



#END OF SDES DECRYPTION ALGORITHM

p10=[3,5,2,7,4,10,1,9,8,6]      #initial permutation box(p-box) for key
p8=[6,3,7,4,8,5,10,9]             #P-box for contaction permutation
p4=[2,4,3,1]        
ip=[2,6,3,1,4,8,5,7]                #initial permutation box
ep=[4,1,2,3,2,3,4,1]               #expansion permutation box
s1=[[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]    #substitution-box 1
s2=[[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]    #substitution-box 2
key='1010000010'
plaintext='11011000'            #First Input String '01100010'


print("Plain Text    : ",plaintext)
ciphertext=sdes_encryption(plaintext,key,ip,ep,s1,s2,p4,p10,p8)
print("Cipher Text  : ",ciphertext)