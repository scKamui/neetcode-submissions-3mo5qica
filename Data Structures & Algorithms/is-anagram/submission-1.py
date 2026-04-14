class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False 
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        
        return True

        

        
        
        
        
        
        
        """sorted_s = "".join(sorted(s))
        sorted_t = "".join(sorted(t))

        if sorted_s == sorted_t:
            return True
        return False
        
        
        set1 = set()
        set2 = set()

        for char in s:
            set1.add(s)
        
        for char in t:
            set2.add(t)

        if set1 == set2:
            return True
        return False """




        