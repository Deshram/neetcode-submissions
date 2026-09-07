class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = Counter(s)
        t_count = Counter(t)

        for c in s_count:
            if not t_count.get(c):
                return False

        for c in t_count:
            if not s_count.get(c):
                return False


        for c in s_count:
            if s_count[c] != t_count[c]:
                return False

        return True


                

             