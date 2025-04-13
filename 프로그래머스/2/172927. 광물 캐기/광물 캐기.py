def solution(picks, minerals):
    answer =0
    fatigue = {
        0: {"diamond": 1, "iron": 1, "stone": 1},
        1: {"diamond": 5, "iron": 1, "stone": 1},
        2: {"diamond": 25, "iron": 5, "stone": 1}
    }
    
    ## 먼저 chunk로 나눈다. 그런다음 제일 높은 chunk순서대로 나열한다
    n = sum(picks)
    m = len(minerals)
    chunks = []
    for i in range(0, min(len(minerals), n*5), 5):
        chunks.append(minerals[i:i+5])
    
    def calc_hardness(chunk):
        return sum(fatigue[2][m] for m in chunk)
                   
    chunks.sort(key=calc_hardness, reverse=True)
    
    pick_order =[]
    for pick_type, count in enumerate(picks):
        pick_order.extend([pick_type]*count)
        
    print(pick_order)
    
    for i in range(len(chunks)):
        if i >= len(pick_order):
            break
        pick = pick_order[i]
        for m in chunks[i]:
            answer+=fatigue[pick][m]
    
    return answer