## 19번째
## 0~9 10개
## 10 / 20 21 / 30 31 32 / 40 41 42 43 / 50 
import sys

sys.setrecursionlimit(1000001)

def is_declining(number: str):
    for val in range(len(number)-1):
        if number[val] <= number[val+1]:
            return False
    return True

N = int(input())
def dfs(node: str, depth):
    # print(node, depth)

    if depth == N:
        return node

    else:
        if depth < 11:
            return dfs(str(int(node)+1), depth+1)
        else:
            ## while문을 통해서 값을 올려보고 그 값이 앞의 값보다 작으면 dfs로 보내야한다
            ## 수의 가장 처음부터 접근하면서 수의 가장 처음보다 작은수의 범위내 에서 작은것 부터 올라가본다
            ## 5 4 3 2 => 6 2 1 0
            ## 1의 자리수를 1 더해보고 아니면
            ## 10의 자리수를 1더해보고 아니면
            ## 100의 자리수를 1더해보는 식으로 하나씩 접근을 한다.
            ## 하지만 여기서 자리수를 올리면 그 뒤에 있는 모든 숫자들은 0으로 바꾸고 최소로 하나씩 올려본다!

            for index in range(len(node)-1, -1, -1):
                newNode = node[:index] + str(int(node[index])+1) + "".join(sorted([str(i) for i in range(len(node)-index-1)], reverse=True))

                if len(newNode) > len(node):
                    newNode = "".join(sorted([str(i) for i in range(0, len(newNode))], reverse=True))

                if is_declining(newNode):
                    return dfs(newNode, depth+1)
            
            return -1

            ## 자리수가 바뀌었을때
            ## 9 8 7 6
            ## 1 0 0 0 0

            ## 맨 앞자리의 숫자는 최소 그 길이-1 정도는 되어야한다!
            ## 즉 맨 앞자리 숫자가 바뀌면 그 최소는 0~길이-1 까지 차례대로 들어가야한다
print(dfs("0",1))
