def solution(N, number):
    answer = 0
    
    ### 5를 5번 사용해서 만들 수 있는 숫자는
    ## 5를 1번 사용한것과 (사칙연산) 5를 4번 사용해서 만드는 숫자
    ## 5를 2번 사용한거과 (사칙연산) 5를3번 사용해서 만드는 숫자
    s = [set() for x in range(9)]
    for i,x in enumerate(s[1:], start=1):
        x.add(int(str(N)*i))

    ## 즉 s[0]에는 s를 1번 사용하여 만들 수 있는 숫자들을 넣을 것이다
    for i in range(1, 9):
        ## j는 N을 1번 ~ N-1번까지 사용해서 만드는 수와 비교
        for j in range(1, i+1):
            for op1 in s[j]:
                for op2 in s[i-j]:
                    s[i].add(op1+op2)
                    s[i].add(op1-op2)
                    s[i].add(op1*op2)
                    if op2 != 0:
                        s[i].add(op1//op2)
        
        ##N을 i+1번 사용할때 찾고자하는 number가 존재하면
        if number in s[i]:
            answer = i
            break
        else:
            answer = -1
    return answer