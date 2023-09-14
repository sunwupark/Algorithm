N, M = map(int, input().split())
lists = []
max = 0

for i in range(N):
    row = input()
    lists.append([rows for rows in row])

for i in range(N-1):
    for j in range(M-1):
        for k in range(1,N):
            if(i+k < N and j+k < M):
                if lists[i][j] == lists[i+k][j] == lists[i][j+k] == lists[i+k][j+k]:
                    if max < (k+1)*(k+1):
                        max = (k+1)*(k+1)

if max == 0:
    print(1)
else:
    print(max)
