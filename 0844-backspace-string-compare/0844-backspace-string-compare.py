class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []

        for i in range(len(s)):
            if stack_s and s[i] == "#":
                stack_s.pop()

            if s[i] != "#":
                stack_s.append(s[i])

        for i in range(len(t)):
            if stack_t and t[i] == "#":
                stack_t.pop()

            if t[i] != "#":
                stack_t.append(t[i])

        return ("".join(stack_s) == "".join(stack_t))

