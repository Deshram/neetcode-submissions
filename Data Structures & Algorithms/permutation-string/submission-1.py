class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = [0]*26
        s2_count = [0]*26

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord("a")] += 1
            s2_count[ord(s2[i]) - ord("a")] += 1

        matches = 0 
        for i in range(26):
            
            if s1_count[i] == s2_count[i]:
                matches+=1
                
        start = 0
        print(start,  matches)
        for end in range(len(s1), len(s2)):
            if matches == 26:
                return True

            #removing start from window
            index = ord(s2[start]) - ord("a")
            
            if s2_count[index] == s1_count[index]:
                matches-=1
                
            elif s2_count[index]-1 == s1_count[index]:
                matches+=1
                
            start += 1
            s2_count[index] -= 1

            #add end to window
            index = ord(s2[end]) - ord("a")
            if s2_count[index] == s1_count[index]:
                matches-=1
                
            elif s2_count[index]+1 == s1_count[index]:
                matches+=1
                
            s2_count[index] += 1

            
        return matches == 26                
                
