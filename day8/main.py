# leet code two sum  1st code 
class Solution:
    def twoSum(self, nums, target):
        nums_ind = {}
        for x, y in enumerate(nums):

            c = target - y
            if c in nums_ind:
                return [nums_ind[c],x]
            nums_ind[y] = x
        return []
nums = [2,7,11,15]
target = 9

a = Solution()

a.twoSum(nums,target)

