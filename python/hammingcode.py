def Encryp(binary):

    l = [0]*7                    #creating an empty list

    binar = binary[::-1]        #reversing the list and filling the binary bits and assigning
    l[0] = "-1"                 #-1 to parity bits
    l[1] = "-1"
    l[2] = binar[0]
    l[3] = "-1"
    l[4] = binar[1]
    l[5] = binar[2]
    l[6] = binar[3]       #if the sum is 1 or 3, that means there are odd no. of '1's
                        #so we need take the parity bit as 1, or else it is 0

    if int(l[2])+int(l[4])+int(l[6]) == 1 or int(l[2])+int(l[4])+int(l[6]) == 3:  # [0,0,1,0,0,1,0]
        l[0] = "1"
    else:
        l[0] = "0"

    if int(l[2])+int(l[5])+int(l[6]) == 1 or int(l[2])+int(l[5])+int(l[6]) == 3:
        l[1] = "1"
    else:
        l[1] = "0"

    if int(l[4])+int(l[5])+int(l[6]) == 1 or int(l[4])+int(l[5])+int(l[6]) == 3:
        l[3] = "1"
    else:
        l[3] = "0"
    st = ""
    for i in l:       #converting list into string
        st += i
    return st[::-1]

###################################################################################################
def Decryp(binary):
    l= list(binary)[::-1]      #if the sum is 1 or 3 after encrytion, that means there is 
                        #mistake in  the message
                        # if it is 2 or 4 , there is no prooblem so we can add '0' or else it is
    st=""                #we should add 1   
    
    if int(l[4])+int(l[5])+int(l[6])+int(l[3]) == 1 or int(l[4])+int(l[5])+int(l[6])+int(l[3]) == 3:
        st += "1"
    else:
        st+="0"
    

    if int(l[2])+int(l[5])+int(l[6])+int(l[1]) == 1 or int(l[2])+int(l[5])+int(l[6])+int(l[1]) == 3:
        st += "1"
    else:
        st += "0"

    
    
    if int(l[2])+int(l[4])+int(l[6])+int(l[0]) == 1 or int(l[2])+int(l[4])+int(l[6])+int(l[0]) == 3:  # [0,0,1,0,0,1,0]
        st+="1"
    else:
        st += "0"                       
    x=int(st,2)                   #we are converting from binary to integer
    return x

##############################################################################################

if __name__ == "__main__":
    bina = input("enter the 4-digit binary")
    res1 = Encryp(bina)

    #tr="1010111"
    res2 = Decryp(res1)  #if we print the commented line, the answer will come between 1 to 7  
    print("the binary code after encoding with parity bits is : "+res1) 
           #indicating it is wrong
    if res2==0:
        print("there is no error while transmitting")
    else:
        print("your message is corrupted and the position of corruption is "+res2)
