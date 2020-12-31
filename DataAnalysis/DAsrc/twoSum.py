class Solution:
    def twoSum(self, nums, target):
        num = []
        for i in range(len(nums)):
            if i ==len(nums) - 1:
                return num
            else:
                for j in range(i+1, len(nums)):
                    temp = nums[i] + nums[j]
                    if temp == target:
                        num.append(i)
                        num.append(j)
                        return num
nums = [2, 7, 11, 15]
target = 9
sl = Solution()
mm = sl.twoSum(nums, target)
print(mm)