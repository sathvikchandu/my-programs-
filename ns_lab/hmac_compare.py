import hmac
import hashlib
import time

t1=time.time()
print("approach 1 we are taking all the always of the k+ as an array to caculate the time ")
kpo=[10110110,10111010,10111110,11011010,11011110,11101010,11101110,11111010]
msg=['attack','on','dawn','get','ready','to','attack','on']
ipad=10110111
ans1=[]
for i in range (len(kpo)):


    res1=str(ipad^kpo[i])
    res1=res1.encode('UTF-8')
    hmac_gen=hmac.new(res1,msg[i].encode('UTF-8'),hashlib.sha256)
    hmac_val=hmac_gen.hexdigest()
    ans1.append(hmac_val)

ans2=[]
opad=10101010
for i in range (len(ans1)):
    res2=str(i^opad)
    res2=res2.encode('UTF-8')
    hmac_gen2=hmac.new(res2,ans1[i].encode('UTF-8'),hashlib.sha256)
    hmac_val2=hmac_gen2.hexdigest()
    ans2.append(hmac_val2)
for i in range(len(ans2)):
    print("the",i,"th hash value is: ",ans2[i])   
t2=time.time()
print()
print("the time taken is: ",t2-t1,"seconds")




