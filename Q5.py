class Solution:
    def longestPalindrome(self, s) -> str:
        temp_max = 0
        final_left = 0
        final_right = 0
        for start in range(len(s)):
            left = start - 1
            right = start + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > temp_max:
                    temp_max = right - left + 1
                    final_left = left
                    final_right = right
                left -= 1
                right += 1

            left = start
            right = start + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > temp_max:
                    temp_max = right - left + 1
                    final_left = left
                    final_right = right
                left -= 1
                right += 1

        return s[final_left: final_right+1]

s = Solution()
print(s.longestPalindrome(s="xabbay"))

