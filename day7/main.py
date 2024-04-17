#leet code practice problem   #1st code
def two_sum(nums,target):

    num_indices = {}

    for i,num in enumerate(nums):
        # print(f"{i},{num}")
        complement = target - num

        if complement in num_indices:
            return [num_indices[complement],i] 
        num_indices[num] = i
        # print("the num of indices",num_indices)

    return []



nums = [2,7,11,15]
target = 26
print(two_sum(nums,target))