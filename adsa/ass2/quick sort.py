def partition(st,comp,arr):
    pidx=st
    pt=arr[pidx]
    

    while st<comp:
        while st<len(arr) and arr[st]<=pt:
            st+=1
        while arr[comp]>pt:             #check for lo and high such that lo<=pt and high>pt
            comp-=1
        if st<comp:
            arr[st],arr[comp]=arr[comp],arr[st]         #swap the values
    arr[pidx],arr[comp]=arr[comp],arr[pidx]         #swap the pt with the comp value
    return comp                             #return the index of the sorted element 


def quick_sort(st,comp,arr):
    
    
    if st<comp:
        j=partition(st,comp,arr)     #partitioning
        quick_sort(st,j,arr)      #calling the left part of the function
        quick_sort(j+1,comp,arr)       #calling the right part of the function
    return arr
   


print("Enter the number of elements as spaced integers: ")
l=list(map(int,input().split()))
res=quick_sort(0,len(l)-1,l)
print("The sorted list is: ",res)
