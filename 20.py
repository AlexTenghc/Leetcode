#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#An input string is valid if:

#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = dict({"}":"{", 
                "]":"[", 
                ")":"("})

        if len(s) % 2 == 1:
            return False

        for i in range(len(s)):


            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.append(s[i])
                
            else:
                if len(stack) == 0:
                    return False
                out = stack.pop()
                if out != dic[s[i]]:
                    return False

        if len(stack) == 0:
            return True
        return False
