K = int(input())
dpA = [1] + [0]*K
dpB = [0] * (K+1)

for i in range(1,K+1):
    dpA[i] = dpB[i-1]
    dpB[i] = dpB[i-1] + dpA[i-1]

print(dpA[K], dpB[K])
