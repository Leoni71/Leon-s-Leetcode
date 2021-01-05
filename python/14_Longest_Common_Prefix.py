# Find the shortest string then compare each character of it with all other strings one by one
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        if not strs:
            return result
        
        shortest = strs[0]
        shortest_len = len(strs[0])
        for str in strs[1:]:
            if len(str) < shortest_len:
                shortest, shortest_len = str, len(str)
        
        for i in range(shortest_len):
            for str in strs:
                if str[i] != shortest[i]:
                    return shortest[:i]
        
        return shortest
