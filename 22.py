"""Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(l, r, s):
            if len(s) == n * 2:
                res.append(s)
                return
            
            if l < n:
                dfs(l + 1, r, s + "(")
            
            if r < l:
                dfs(l, r+1, s + ")")

        res = []
        dfs(0, 0, "")
        return res
