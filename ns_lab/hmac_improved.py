import hmac
import hashlib
import time

t1=time.time()
print("approach 2 we are already pre computer the xor values and only performing hash functions evry time ")
kpos=10110110
msg=['attack','on','dawn','get','ready','to','attack','on']
ipad=10110111
ans1=[]
res1=str(ipad^kpos)
res1=res1.encode('UTF-8')
for i in range(len(msg)):

    
    hmac_gen=hmac.new(res1,msg[i].encode('UTF-8'),hashlib.sha256)
    hmac_val=hmac_gen.hexdigest()
    ans1.append(hmac_val)

ans2=[]
opad=10101010

res2=str(kpos^opad)
res2=res2.encode('UTF-8')
for i in range (len(ans1)):
    
    hmac_gen2=hmac.new(res2,ans1[i].encode('UTF-8'),hashlib.sha256)
    hmac_val2=hmac_gen2.hexdigest()
    ans2.append(hmac_val2)
for i in range(len(ans2)):
    print("the",i,"th hash value is: ",ans2[i])   
t2=time.time()
print("the time taken is: ",t2-t1)




