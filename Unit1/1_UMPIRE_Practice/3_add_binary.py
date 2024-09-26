print(int("110", 2))  # This will return the integer 6
Because 1×2**2 +1×2**1 +0×2**0  =4+2+0=6
so basically, int(a,2) convert binary to number and bin(4) convert #number to binary
bin(4) --> converts number 4 to Binary which is 0b100
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2:]
so, basically int("1101", 3) means
3**3*1 + 3**2 *1 + 3**1 *0 + 3**0 *1?
