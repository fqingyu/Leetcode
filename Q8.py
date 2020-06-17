import re
class Solution:
    def myAtoi(self, str: str) -> int:
        num_str = re.findall(r'(^[-+]?[0-9]*)', str.lstrip())
        INT_MAX = 2 ** 31 - 1
        INT_MIN = - 2 ** 31
        # return num_str
        try:
            num = int(num_str[0])
            if num > INT_MAX:
                num = INT_MAX
            if num < INT_MIN:
                num = INT_MIN
            return num
        except Exception:
            return 0

test = Solution()
print(test.myAtoi("-"))