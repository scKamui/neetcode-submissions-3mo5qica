class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sorted_s = "".join(sorted(s))
        sorted_t = "".join(sorted(t))

        if sorted_s == sorted_t:
            return True
        return False
        
        
        """set1 = set()
        set2 = set()

        for char in s:
            set1.add(s)
        
        for char in t:
            set2.add(t)

        if set1 == set2:
            return True
        return False """




        