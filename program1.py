def smallest_missing_positive_integer(nums: List[int]) -> int:
    maxx= max(nums) 
    if maxx < 1:


        return 1
    if len(nums) == 1:
        return 2 if nums[0] == 1 else 1
    l = [0] * maxx
    for i in range(len(nums)):
        if nums[i] > 0:
            if l[nums[i] - 1] != 1:

                
                l[nums[i] - 1] = 1
    for i in range(len(l)):


        if l[i] == 0:
            return i + 1
        
    return i + 2








    



  

