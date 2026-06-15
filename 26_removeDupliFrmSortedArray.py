class Solution(object):
    def removeDuplicates(self, nums):
        slow = 0

        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]

        return slow + 1


nums = [1, 1, 2, 2, 3, 4, 4, 5]

sol = Solution()
k = sol.removeDuplicates(nums)

print("Number of unique elements:", k)
print("Array after removing duplicates:", nums[:k])