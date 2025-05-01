def solution(s):
    answer = 0
    pairs = {"[":"]", "{":"}", "(":")"}
    from collections import deque
    
    for i in range(len(s)):
        curr = s[i:] + s[:i]
        stack = deque()
        right = True
        for j in range(len(s)):
            if curr[j] in pairs:
                stack.append(curr[j])
            else:
                if not stack:
                    right = False
                    break
                elif curr[j] == pairs[stack[-1]]:
                    stack.pop()
                else:
                    right = False
                    break
        if right and not stack:  # 스택이 비어 있어야 완전히 올바른 괄호 문자열
            answer += 1
    return answer