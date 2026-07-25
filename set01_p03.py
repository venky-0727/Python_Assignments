n = list(map(int, input().split())) # 10 30 20 50 40
def secondLargest(nums):
    largest = n[0] #10 
    second_largest = n[0] # 10 
    for i in range(len(nums)):
        if largest <= nums[i]:# 10 <= 10,10 <= 30 
            largest = nums[i] # l = 10 , l=30 
        elif second_largest <=largest : # 10 <= 10, 10 <= 30 
            second_largest = largest # 10 s_l = 30 
    if largest == second_largest: #10 == 10  30 
        return "No Second largest"
    return f"{'Second largest = '}{second_largest}"
result = secondLargest(n)
print(result)