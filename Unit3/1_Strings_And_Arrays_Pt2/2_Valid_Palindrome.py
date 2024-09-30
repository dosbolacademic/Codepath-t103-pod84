class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ("".join([i for i in s if i.isalnum()])).lower()
        
        l=0
        r=len(s)-1

        while l<=r:
            if s[l]!=s[r]:
                return False
            else:
                l+=1
                r-=1
        return True

        
