import sys
N = int(sys.stdin.readline().strip())

result = -1
for i in range(N//5, -1, -1):
    value = N-(5*i)
    if value%2 ==0:
        result = value//2 + i
        break

print(result)