class Solution(object):
    def moveZeroes(self, nums):
        left = 0
        length = len(nums)

        for right in range(length):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

        return nums

nums = [0, 1, 0, 3, 12]

sol = Solution()
result = sol.moveZeroes(nums)

print("Array after moving zeros:")
print(result)