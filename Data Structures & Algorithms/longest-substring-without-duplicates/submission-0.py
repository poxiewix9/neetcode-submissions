class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = {}
        start = 0
        maxCount = 0
        
        for i in range(len(s)):
            if s[i] in hash_map and hash_map[s[i]] >= start:
                start = hash_map[s[i]] + 1
            
            hash_map[s[i]] = i
            
            maxCount = max(maxCount, i - start + 1)
            
        return maxCount