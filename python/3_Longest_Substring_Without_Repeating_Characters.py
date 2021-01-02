class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        start = end = result = 0
        characters = set()
        while end < length:
            if s[end] not in characters:
                characters.add(s[end])
                end += 1
                result = max(result, end-start)
            else:
                characters.remove(s[start])
                start += 1
                
        return result
