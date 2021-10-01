def countVowelPermutation(n):
   
    # To avoid the large output value
    mod =  1e9 + 7
 
    # Initialize 2D dp array
    dp = [[0 for i in range(5)] for j in range(n + 1)]
     
    # Initialize dp[1][i] as 1 since
    # string of length 1 will consist
    # of only one vowel in the string
    for i in range(5):
        dp[1][i] = 1
     
    # Directed graph using the
    # adjacency matrix
    mat = [[1],[0, 2], [0, 1, 3, 4], [2, 4],[0]]
 
    # Iterate over the range [1, N]
    for i in range(1, n, 1):
       
        # Traverse the directed graph
        for u in range(5):
            dp[i + 1][u] = 0
 
            # Traversing the list
            for v in mat[u]:
               
                # Update dp[i + 1][u]
                dp[i + 1][u] += dp[i][v] % mod
 
    # Stores total count of permutations
    res = 0
    for i in range(5):
        res = (res + dp[n][i]) % mod
 
    # Return count of permutations
    return int(res)
 


N = int(input())
print(countVowelPermutation(N))