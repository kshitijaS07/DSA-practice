class Solution(object):
    def singleNumber(self, nums):
        result = 0

        for num in nums:
            result ^= num

        return result


# Driver Code
nums = [4, 1, 2, 1, 2]

sol = Solution()
answer = sol.singleNumber(nums)

print("The single number is:", answer)