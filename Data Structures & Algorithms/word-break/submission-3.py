class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        visited = {}

        def dfs(curr_word, curr_dict_word, rem_s):
            if len(rem_s) == 0:
                return True
            elif curr_word in visited:
                return visited[curr_word]            

            curr_word = "" # Build up the new word, once we arrive at one similar to 
            res = False
            for char_index in range(len(rem_s)):
                curr_word+=rem_s[char_index]
                # Compare it with each word that we have in dict
                for dict_word in wordDict:
                    if curr_word == dict_word:
                        print(len(rem_s[char_index+1::]))
                        res = dfs(curr_word, dict_word, rem_s[char_index+1::])
                        visited[curr_word] = res
                        if res == True:
                            return res
                    
                
            
            return res
            
        return dfs("", "", s)