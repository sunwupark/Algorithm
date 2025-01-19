plate = []

dx = [1, 0, 1, -1]  # 오른쪽, 아래, 오른쪽 아래 대각선, 오른쪽 위 대각선
dy = [0, 1, 1, 1]

# 바둑판 입력
for _ in range(19):
    plate.append(list(map(int, input().split())))

# 바둑판 탐색
for curX in range(19):
    for curY in range(19):
        if plate[curX][curY] == 1 or plate[curX][curY] == 2:
            currentValue = plate[curX][curY]
            # 4개의 방향 탐색
            for direction in range(4):
                nx, ny = curX, curY
                count = 1

                # 한 방향으로 같은 색의 돌을 체크
                while True:
                    nx += dx[direction]
                    ny += dy[direction]

                    if 0 <= nx < 19 and 0 <= ny < 19 and plate[nx][ny] == currentValue:
                        count += 1
                    else:
                        break

                # 반대 방향도 체크
                nx, ny = curX - dx[direction], curY - dy[direction]
                if 0 <= nx < 19 and 0 <= ny < 19 and plate[nx][ny] == currentValue:
                    continue  # 반대 방향으로 연결된 돌이 있으면 무효

                # 정확히 다섯 개인 경우 출력
                if count == 5:
                    print(currentValue)
                    print(curX + 1, curY + 1)  # 1-based index
                    exit()

# 승부가 결정되지 않은 경우
print(0)