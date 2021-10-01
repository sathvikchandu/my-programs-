def main(st):
    res=""
    for i in range(len(st)):
        
        count=1
        
        if st[i-1]==st[i]:
            continue
        else:
            res+=st[i]
            while i+1<len(st) and st[i]==st[i+1]:
                count+=1
                
                i+=1
                
            if count>1:
                res+=str(count)
    return res
    




if __name__ == "__main__":
    s= input()
    print(main(s))