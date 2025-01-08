sentence = input()

def printTemp(temp: str):
    if temp.strip():  # temp가 비어있거나 공백만 포함된 경우 처리 방지
        splitedTemp = temp.split()
        for i, word in enumerate(splitedTemp):
            if i == len(splitedTemp) - 1:
                print(word[::-1], end="")  # 마지막 단어
            else:
                print(word[::-1], end=" ")  # 중간 단어 뒤 공백 추가


def solve(sentence: str):
    i = 0
    temp = ""
    while i < len(sentence):
        if sentence[i] == "<":  # 태그 시작
            printTemp(temp)  # 태그 이전 단어 처리
            temp = ""  # temp 초기화

            # 태그 출력
            while sentence[i] != ">":
                print(sentence[i], end="")
                i += 1
            print(sentence[i], end="")  # '>' 출력
            i += 1
        else:
            # 태그 외부 단어 처리
            if sentence[i] == " ":  # 공백 발견 시 현재 단어 뒤집기
                printTemp(temp)
                print(" ", end="")  # 공백 출력
                temp = ""  # temp 초기화
            else:
                temp += sentence[i]
            i += 1

    # 루프 종료 후 남은 temp 처리
    printTemp(temp)


# 실행
solve(sentence)