class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for s in strs:
            ret += (str(len(s))) + "#" + s
        print(ret)
        return ret
    
    def decode(self, s: str) -> List[str]:
        ret = []
        l = r = 0
        
        while l < len(s):
            r = l
            while s[r] != "#":
                r += 1
            length = int(s[l:r])
            ret.append(s[r+1:r+length+1])
            l = r + length + 1
        return ret
