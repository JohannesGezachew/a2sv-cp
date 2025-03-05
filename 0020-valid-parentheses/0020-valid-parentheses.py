class Solution:
    def isValid(self, s: str) -> bool:
        container  = {")":"(" , "]":"[", "}":"{"}
        stack = []

        for i in range(len(s)):
            if s[i] in container:
                if not stack or container[s[i]] != stack.pop():
                    return False      
            else:
                stack.append(s[i])
            
        return False if stack else True

