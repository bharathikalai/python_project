#leet code practice problem 1
def two_sum(nums,target):

    num_indices = {}

    for i,num in enumerate(nums):
        complement = target - num

        if complement in num_indices:
            return [num_indices[complement],i]
        num_indices[num] = i

    return []



nums = [2,7,11,15]
target = 9

print(two_sum(nums,target))