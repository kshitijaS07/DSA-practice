class Solution(object):
    def isPalindrome(self, x):
        # Negative numbers are never palindromes
        if x < 0:
            return False

        # Convert to string
        s = str(x)

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True


# Driver Code
num = int(input("Enter a number: "))

sol = Solution()
result = sol.isPalindrome(num)

print("Is the number a palindrome?", result)