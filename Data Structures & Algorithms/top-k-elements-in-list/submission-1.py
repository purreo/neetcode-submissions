class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap + heap
        # bucketsort
        count = Counter(nums)
        freq = [[] for i in range(len(nums)+1)]

        for num, cnt in count.items():
            freq[cnt].append(num)

        ans = []
        for i in reversed(range(len(freq))):
            ans.extend(freq[i])
            if len(ans) == k: 
                return ans

           