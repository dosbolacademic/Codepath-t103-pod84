class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        res =""
        f = strs[0]

        for i in range(len(f)): # I took length of first word
            for j in strs: 
                if i>=len(j) or j[i]!=f[i]:
                    return res
            res+=f[i]
        return res
