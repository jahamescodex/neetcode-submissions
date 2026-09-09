class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        memory = defaultdict(list)

        for s in strs:
            count = [0] * 26 # constant time
            # + 
            for char in s:
                count[ord(char)-ord('a')] += 1
            
            memory[tuple(count)].append(s)
        
        return list(memory.values())