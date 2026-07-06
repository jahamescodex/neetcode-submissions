class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
    
        my_dictS, my_dictT = {}, {}

        for idx in range(len(s)):
            my_dictS[s[idx]] = 1 + my_dictS.get(s[idx], 0)
            my_dictT[t[idx]] = 1 + my_dictT.get(t[idx], 0)
    
        if my_dictS != my_dictT:
           return False
    
        return True


        # 0 : r
        # 1 : a
        # 2 : c
        # 3 : e
        # 4 : c
        # 5 : a
        # 6 : r