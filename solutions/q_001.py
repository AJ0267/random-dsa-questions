# Two sum with given target.

def two_sum(nums, target):
    num_map = {} 
    for i in range(len(nums)): 
        diff = target - nums[i]  # diff    
        if diff in num_map: 
            return [num_map[diff], i]      
        num_map[nums[i]] = i     
    return [] 

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target)) 