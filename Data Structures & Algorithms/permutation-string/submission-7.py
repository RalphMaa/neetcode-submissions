class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        
        key_s1 = {}
        for char in s1:
            key_s1[char] = 1 + key_s1.get(char, 0)
                
        window = len(s1)
        i = 0
        while i + window <= len(s2):
            key_s2 = {}
            for char in s2[i:i+window]:
                key_s2[char] = 1 + key_s2.get(char, 0)
            
            if key_s2 == key_s1:
                return True
            
            i+=1
        
        return False
            

        
