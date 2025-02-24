def solution(nums):
    answer = 0
    
    new_nums = len(set(nums))
    number = len(nums)//2
    answer = min(new_nums, number)
    
    return answer