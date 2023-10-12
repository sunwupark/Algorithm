from itertools import combinations

N,S = map(int, input().split())
input_list = list(map(int, input().split()))
sums = 0

for i in range(1, N+1):
    temp_list = list(combinations(input_list, i))
    for j in temp_list:
        if sum(j) == S:
            sums += 1

print(sums)
            