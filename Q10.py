class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        print("str:{}, pattern:{}".format(s, p))
        if not p:
            return not s
        elif p:
            if len(p) >= 2 and p[1] == '*':
                # if not self.isMatch(s, p[2:]):
                #     if s[1:] and s[1] == s[0]:
                #         return self.isMatch(s[1:], p)
                #     elif s[1:] and s[1] != s[0] and p[0] == '.':
                #         return self.isMatch(s[1:], p)
                #     return self.isMatch(s[1:], p[2:])
                if not self.isMatch(s, p[2:]):
                    return self.isMatch(s[1:], p[2:])
                else:
                    return self.isMatch(s[1:], p)
            else:
                if s:
                    if p[0] == s[0] or p[0] == '.':
                        return self.isMatch(s[1:], p[1:])
                elif not s:
                    return False


test = Solution()
print(test.isMatch('aab', '.*c*a*b'))


