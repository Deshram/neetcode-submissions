class Solution:
    def hammingWeight(self, n: int) -> int:
        b = ""
        while n :
            rem = n%2
            b = str(rem) + b
            n = n // 2
        
        count = 0
        
        for c in b:
            if c == "1":
                count+=1

        return count