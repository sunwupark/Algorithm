N, K = map(int, input().split())
objectList = []
for i in range(N):
    W,V = map(int, input().split())
    objectList.append((W,V))

dp = [0] * (K+1)

# 뒤에서 부터 계산을 한다

for w,v in objectList:
    for j in range(K, w-1, -1):
        dp[j] = max(dp[j], dp[j-w] + v)

print(dp[K])
