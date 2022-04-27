import hmac
import hashlib
key="this is a secret key"        #this is the key
message=input("Enter the message u want to send: ")    #user message
encoded_key=key.encode()       #encoding the key to make sure the equal no. of chars are present

hmac_gen=hmac.new(encoded_key,message.encode('UTF-8'),hashlib.sha256)  # performing E(K,M) operation

digest_val=hmac_gen.hexdigest()  #converting the value to hexadecimal
digest_val=digest_val[3:]

print("The digest value is: ",digest_val)


#since only the sender side is asked, digest_val will be the final answer.


