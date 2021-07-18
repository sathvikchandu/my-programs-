import sys
for i in range (int(input())):
    n=int(input())
    if n>0:
        z= str(n)
        y= list(z)
        co=0
        for i in y:
            if i=='0' or i=='1':
                co+=1
        if co ==len(y):
            print("1")
            sys.exit()

        if n%10==1:
            s=str(n)
            le=len(s)
            st1= ""
            for i in range(le):
                st1+='1'
            re=n-int(st1)
            rem= re/10
            print(int(rem+1))
        else:
            s=str(n)
            le=len(s)
            st1= ""
            for i in range(le):
                st1+='1'
            re=n-int(st1)
            if re>10:

                rem= re/10
                count= rem+1
                re= re-rem*10
                count= count+re
                print(count)
                sys.exit()
            else:

                print(re+1)


