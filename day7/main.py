# #leet code practice problem   #1st code
# def two_sum(nums,target):

#     num_indices = {}

#     for i,num in enumerate(nums):
#         # print(f"{i},{num}")
#         complement = target - num

#         if complement in num_indices:
#             return [num_indices[complement],i] 
#         num_indices[num] = i
#         # print("the num of indices",num_indices)

#     return []



# nums = [2,7,11,15]
# target = 26
# print(two_sum(nums,target))



class Solution:
    def __init__(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        """
        self.nums = nums
        self.target = target

    def twoSum(self):
        """
        :rtype: List[int]
        """
        dic = {}
        for i, x in enumerate(self.nums):
            c = self.target - x

            if c in dic:
                return [dic[c], i]
            dic[x] = i
        return []

num = [2, 7, 11, 15]
target = 9

test = Solution(num, target)

x = test.twoSum()

print(x, "the value of x")
