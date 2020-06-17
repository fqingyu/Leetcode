class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        positive_flag = 1
        if x[0] == '-':
            positive_flag = 0
            x = x[1:]
        num = ""
        itr = len(x) - 1
        while itr >= 0:
            num += x[itr]
            itr -= 1
        num = int(num)
        if num >= 2 ** 31:
            num = 0
        if positive_flag == 0:
            num = -num
        return num

test = Solution()
print(test.reverse(1534236469))