def count(nums):
    count=0
    for num in nums:
        if num == 2:
            count = count + 1
    return count
print(count([1,2,3,2,1,5,6,3,4,2]))
            
