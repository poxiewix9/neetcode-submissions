class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solution = defaultdict(list)

        for s in strs:
            letterFreq = [0] * 26
            for char in s:
                letterFreq[ord(char) - ord('a')] += 1
            solution[tuple(letterFreq)].append(s)
        
        return list(solution.values())

