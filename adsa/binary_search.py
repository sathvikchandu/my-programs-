def binary_search(l,n):
    lo=0
    h=len(l)-1          
    
    
    
    while lo<=h:
        mid=(lo+h)//2
        
        if l[mid]<n:   #if the element is greater the middle element then search on the right side
            lo=mid+1
        elif l[mid]>n:  #the element is less than the middle element then search on the left side
            h=mid-1
        else:
            return mid  #if the element is found then return the index
    return "Not Found"
        
    


if __name__ == '__main__':
    print("Enter the number of elements in the list with spaced integers")
    l= list(map(int,input().split()))
    l.sort #even if the list is not sorted, the sort() method is used to sort the list in ascending order.
    n= int(input("Enter the element to find: "))
    res=binary_search(l,n)

    if res=="Not Found":
        print("Element not found")
    else:
        print("Element found at index: ",res+1)