N = int(input())
input_list = []

dp = [[0,0,0]]
for i in range(1,N+1):
    input_list = list(map(int, input().split()))
    temp_list = [0,0,0]
    temp_list[0] = min((dp[i-1][1] + input_list[0]), dp[i-1][2] + input_list[0])
    temp_list[1] = min((dp[i-1][0] + input_list[1]), dp[i-1][2] + input_list[1])
    temp_list[2] = min((dp[i-1][0] + input_list[2]), dp[i-1][1] + input_list[2])
    dp.append(temp_list)   
print(min(dp[N]))