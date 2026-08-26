class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freqList = [[] for x in range(len(nums) + 1)]
        for n in nums:
            count[n] = 1 + count.get(n,0)

        for x in count.items():
            freqList[x[1]].append(x[0])

        finalAnswer = []

        for arr in reversed(freqList):
            for num in arr:
                finalAnswer.append(num)
                if (len(finalAnswer) == k):
                        return finalAnswer
            


    
