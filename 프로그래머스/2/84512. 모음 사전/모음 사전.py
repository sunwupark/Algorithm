def solution(word):
    answer = 0
    alpha = ['A', 'E', 'I', 'O', 'U']
    
    ## 맨앞이 E면 A로 시작하는 모든 단어들을 계산해야한다!
    # A____ 1 + 5 + 5*5 + 5*5*5 + 5*5*5*5 
    # + EA___/EE___ 1 + 2 + 2*5 + 2*5*5 + 2*5*5*5 
    # + EIA,E,I__ 3 + 3*5 + 3*5*5 + 1
    n = len(word)
    for i in range(n):
        ## 첫번쨰 단어에서 가능한 모든 범위를 구한다
        target = alpha.index(word[i])
        index =0 
        answer += (target-index) * ((pow(5, 5-i) -1)/4) + 1
            
        # print(answer)
            
    return answer