
def xor(a, b):                              #xor gunction
   
    
    result = []
   
    #takes 4 bits as input and performs xor operation
    #on last 3 bits as 1st bit is igno red
    for i in range(1, len(b)):              
        if a[i] == b[i]:                   
            result.append('0')
        else:
            result.append('1')
   
    return ''.join(result)     
    #returns the resultant xor bit             

def crc(binary,divisor):
    i=0                           #i and b are variables taken to modify the string
    b=3 
                        #since a 4 digit divisor is taken, 3 zeroes are added to string                        
    binary+="000"
    o= xor(binary[i:b+1],divisor)  #taking 4 characters of string and passing
                                    # them to the function
    b+=1
    divisor1="0000"
    
    for i in range(b,len(binary)):
        o1=o+binary[i]
        #the problem here is the when 0 occurs at first position, the for loop counts it and 
        #in the end, somr cases are missed, i.e all the string is not computed
        #to overcome it, a while loop is placed to calculate the left over bits 
        #final answer is outputed
        if o1[0]=='0':
            o= xor(o1,divisor1)
        else:
            o= xor(o1,divisor)
    
    return o                                                  
        

def decre(binary,divisor):
    i=0
    b=3
    
    
    o= xor(binary[i:b+1],divisor)
    b+=1
    divisor1="0000"
    count=0
    for i in range(b,len(binary)-1):
        o1=o+binary[i]
        #the procedure is same as the above function except the 0's are not included
        # not added at the end       
        if o1[0]=='0':
            count+=1
            o= xor(o1,divisor1)
        else:
            o= xor(o1,divisor)
    i= len(binary)-1
    while count>0:
        
        o1=o+binary[i]
        if o1[0]=='0':
            count+=1
            o= xor(o1,divisor1)
        else:
            o= xor(o1,divisor)
        i+=1
        count-=1
        
    return o 



           
if __name__ == "__main__":

    bina= input("enter the binary")         #inputs
    divi= input("enter a 4 bit divior")      #inputs
    res=crc(bina,divi)                       #function call
    bina+=res                                #binry code generated from transmitters end
    finalres= decre(bina,divi)                 
    if finalres=="000":                      #checking if the final remainder is 000
        print("yes, the msg. is transmitted without interuption or getting corrupted")
    else:
        print("NO, your message is corrupted")
