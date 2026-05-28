class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ""
        for x in strs:
            result += x + "π"
        return result

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        s = s[:-1]
        
        return s.split("π")