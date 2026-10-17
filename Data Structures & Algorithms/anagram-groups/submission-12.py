class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        nums_hash = defaultdict(list) #ID is the num of characters for the string

        for i in strs:
            curr_key = [0 for i in range(26)]
            for j in i:
                # Find the curr_key
                curr_key[ord(j)-ord("a")] += 1
            
            nums_hash[tuple(curr_key)].append(i)
        
        return list(nums_hash.values())

