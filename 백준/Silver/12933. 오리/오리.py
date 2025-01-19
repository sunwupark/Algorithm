duck = {"q": 1, "u": 2, "a": 3, "c": 4, "k": 5}
sentence = input()
totalDucks = []

maxCount = 0

for i in sentence:
    # duck에 없는 문자는 에러 처리
    if i not in duck:
        print(-1)
        exit()

    # 새롭게 q가 나온다면 리스트에 추가
    if i == "q":
        totalDucks.append(1)
    else:
        changed = False
        # 뒤에서부터 순회하면서 소리를 체크
        for j in range(len(totalDucks) - 1, -1, -1):
            if totalDucks[j] + 1 == duck[i]:
                totalDucks[j] = duck[i]
                changed = True
                if totalDucks[j] == 5:
                    del totalDucks[j]
                break

        # 소리를 연결할 수 없다면 중단
        if not changed:
            print(-1)
            exit()

    # 최대 동시 진행 카운트 갱신
    maxCount = max(maxCount, len(totalDucks))

# 모든 소리가 완료되었는지 확인
if len(totalDucks) == 0:
    print(maxCount)
else:
    print(-1)