x, y=input().split()
x= int(x)
y= float(y)
if(x%5==0):
    if(y>=x+0.5):
        print("{:.2f}".format(y-x-0.5))
    else:
        print(y)
else:
    print(y)