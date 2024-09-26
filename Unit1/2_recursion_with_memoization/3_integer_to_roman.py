In Python, dictionary entries are defined using curly braces {} or tuples with commas
class Solution:
    def intToRoman(self, num: int) -> str:
        #we need a Stack to solve this problem, inside of array we need tuple which separate #value and key with commas
        stack = [(1000,"M"), 
                 (900,"CM"),
                 (500,"D"),
                 (400,"CD"),
                 (100,"C"),
                 (90,"XC"),
                 (50,"L"),
                 (40,"XL"),
                 (10,"X"),
                 (9,"IX"),
                 (5,"V"),
                 (4,"IV"),
                 (1,"I")]
        count = 0
        res = ""
        for value, key in stack:
            #We just divide num to 1000 and so on
            count = num//value 

            #we multiply it to key and add it to res
            res+=count*key
            
            #we need to update our num, so it means 1994%1000 --> 994 and so on
            num%=value
        return res
