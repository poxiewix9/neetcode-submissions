class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        pastAnswers = set()
        for x in nums:
            if x in pastAnswers:
                return true
            pastAnswers.add(x)
        
        return false
            
        