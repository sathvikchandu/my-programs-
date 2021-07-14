


n = int(input())
for i in range(n):
    s = input()
    c=0
    if(s[0]=='1'):
        c= c+1
    for i in range(1,len(s)):
        if(s[i]=='1' and s[i]!=s[i-1]):
            c= c+1
    print(c)
