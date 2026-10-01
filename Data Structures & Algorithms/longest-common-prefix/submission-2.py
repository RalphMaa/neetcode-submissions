class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        com_prefix = ""
        for i in range(0, len(strs[0])):
            count = 1
            for j in range(1, len(strs)):
                if i<len(strs[j]):
                    if strs[0][i] == strs[j][i]:
                        count += 1
            if count == len(strs):
                com_prefix += strs[0][i]
            else:
                return com_prefix

            
        return com_prefix
        