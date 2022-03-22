class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {
            "{": "}",
            "(": ")",
            "[": "]"
        }
        stack = []
        start = list(d.keys())
        close = list(d.values())

        for ch in range(len(s)):

            if s[ch] in start:
                stack.append(ch)

            elif s[ch] in close:
                st = stack.pop()

                if stack == [] or d[st] != s[ch]:
                    return False
        return (stack == [])
s=Solution()
print(s.isValid("(]"))