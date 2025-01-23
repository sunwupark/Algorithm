import copy

def rotate(lists: list, d: int, n: int):
    newlists = copy.deepcopy(lists)  # 초기화
    steps = abs(d) // 45  # 45도 단위로 회전

    for _ in range(steps):
        previousLists = copy.deepcopy(newlists)

        # 좌표 생성
        mainDiag = [(k, k) for k in range(n)]  # 주 대각선
        middleCol = [(k, n // 2) for k in range(n)]  # 가운데 열
        subDiag = [(k, n - k - 1) for k in range(n)]  # 부 대각선
        middleRow = [(n // 2, k) for k in range(n)]  # 가운데 행

        if d > 0:  # 시계 방향
            # 주 대각선 -> 가운데 열
            for i in range(n):
                newlists[middleCol[i][0]][middleCol[i][1]] = previousLists[mainDiag[i][0]][mainDiag[i][1]]
            # 가운데 열 -> 부 대각선
            for i in range(n):
                newlists[subDiag[i][0]][subDiag[i][1]] = previousLists[middleCol[i][0]][middleCol[i][1]]
            # 부 대각선 -> 가운데 행
            for i in range(n):
                newlists[middleRow[n - i - 1][0]][middleRow[n - i - 1][1]] = previousLists[subDiag[i][0]][subDiag[i][1]]
            # 가운데 행 -> 주 대각선
            for i in range(n):
                newlists[mainDiag[i][0]][mainDiag[i][1]] = previousLists[middleRow[i][0]][middleRow[i][1]]

        elif d < 0:  # 반시계 방향
            # 주 대각선 -> 가운데 행
            for i in range(n):
                newlists[middleRow[i][0]][middleRow[i][1]] = previousLists[mainDiag[i][0]][mainDiag[i][1]]
            # 가운데 열 -> 주 대각선
            for i in range(n):
                newlists[mainDiag[i][0]][mainDiag[i][1]] = previousLists[middleCol[i][0]][middleCol[i][1]]
            # 부 대각선 -> 가운데 열
            for i in range(n):
                newlists[middleCol[i][0]][middleCol[i][1]] = previousLists[subDiag[i][0]][subDiag[i][1]]
            # 가운데 행 -> 부 대각선
            for i in range(n):
                newlists[subDiag[n - i - 1][0]][subDiag[n - i - 1][1]] = previousLists[middleRow[i][0]][middleRow[i][1]]

    return newlists


# 입력 처리
T = int(input())
result = []

for _ in range(T):
    N, D = map(int, input().split())
    tempList = [list(map(int, input().split())) for _ in range(N)]

    rotated_matrix = rotate(tempList, D, N)

    # 결과 저장
    for row in rotated_matrix:
        result.append(" ".join(map(str, row)))

# 결과 출력
print("\n".join(result))