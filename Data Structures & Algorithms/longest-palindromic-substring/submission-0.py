class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        resLen = 0
        resIdx = (0,0)
        
        for i,c in enumerate(s):
            l,r = i,i

            while l - 1 >= 0 and r + 1 < n and s[l-1] == s[r+1]:
                l -= 1
                r += 1

                if resLen < r-l+1:
                    resLen = r-l+1
                    resIdx = (l,r)
                    print(resIdx)

            l,r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                if resLen < r-l+1:
                    resLen = r-l+1
                    resIdx = (l,r)
                    print(resIdx)
                l -= 1
                r += 1
        
        return s[resIdx[0]:resIdx[1]+1]
        