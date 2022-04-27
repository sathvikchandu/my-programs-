
"""
l= list(map(int,input().split()))
print(l.sort())                      # sort() method is used to sort the list in ascending order.
"""
#manual sorting
def mergelist(arr,l,m,r):
    middle=m-l+1
    ri=r-m

    left=[0]*middle
    right=[0]*ri

    for i in range(0,middle):
        left[i]=arr[l+i]
    
    for j in range(0,ri):
        right[j]=arr[m+1+j]
    
    i=0
    j=0
    k=l

    while i<middle and j<ri:
        if left[i]<=right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
        k+=1
    
    while i<middle:
        arr[k]=left[i]
        k+=1
        i+=1
    
    while j<ri:
        arr[k]=right[j]
        k+=1
        j+=1





def divideconquer(arr,l,r):
    if l<r:
        m=int((l+r)//2)
        divideconquer(arr,l,m)
        divideconquer(arr,m+1,r)     #divideconquer(arr,l,m) and divideconquer(arr,m+1,r) are called recursively.
        mergelist(arr,l,m,r)        #mergelist(arr,l,m,r) is called to mergelist the two sorted subarrays.



if __name__ == '__main__':
    print("Enter the number of elements as spaced integers: ")
    arr=list(map(int,input().split()))
    divideconquer(arr,0,len(arr)-1)
    print(arr)