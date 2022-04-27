def shellsort(l1):
    gap=len(l1)//2

    while gap>0:
        i=0
        j=gap
        while j<len(l1):
            if l1[i]>l1[j]:
                l1[i],l1[j]=l1[j],l1[i]
            i+=1
            j+=1

            r=i
            while r-gap>-1:
                if l1[r-gap]>l1[r]:
                    l1[r-gap],l1[r]=l1[r],l1[r-gap]
                r-=1
        gap=gap//2







if __name__ == '__main__':
    print("Enter the number of elements as spaced integers: ")
    l=list(map(int,input().split()))
    shellsort(l)
    print(l)