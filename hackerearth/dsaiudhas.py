def check_length(n):

	
	ans = 0
	
	while (n):

		
		n = n >> 1

		
		ans += 1

	
	return ans



def check_ith_bit(n, i):

	
	if (n & (1 << (i - 1))):
		return True
	else:
		return False



def no_of_flips(n):

	
	ln = check_length(n)

	
	ans = 0

	
	right = 1

	
	left = ln

	while (right < left):

		
		if (check_ith_bit(n, right) !=
			check_ith_bit(n, left)):
			ans += 1

		
		
		left -= 1

		
		
		right += 1

	
	
	return ans


for _ in range(int(input())):
    #m,k = map(int,input().split())
    n= input()
    n=int(n,2)
    print(res=no_of_flips(n))

    #if res==k:
        #print("YES")
    #else:
        #print("NO")


