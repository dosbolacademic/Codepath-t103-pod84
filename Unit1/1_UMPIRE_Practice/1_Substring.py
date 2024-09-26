full = "meow"
short = "cat"

class Solution:
    def Substring(self, full, short):
        if len(full)<len(short):
            return False
        l=0
        res=0
        for i in range(len(full)):
            if(i<len(full) and l<len(short) and full[i]==short[l]):
                l+=1 
                res = max(res,l)
            else:
                l=1
        
        return res==len(short)


solution = Solution()
print(solution.Substring(full,short))



class Solution:
    def Substring(self, full, short):
        if len(full) < len(short):
            return False
        
        # Check if short is a substring of full using the 'in' keyword
        return short in full

solution = Solution()
print(solution.Substring(full, short))
