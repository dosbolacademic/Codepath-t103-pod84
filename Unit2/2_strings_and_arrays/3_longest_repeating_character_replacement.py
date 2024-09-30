class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        count = [0] *26

        for r in range(len(s)):
            count[ord(s[r])-ord('A')]+=1
            res = max(res,count[ord(s[r])-ord('A')])

            while (r-l+1)-res>k:
                count[ord(s[l])-ord('A')]-=1
                l+=1
        return len(s)-l
