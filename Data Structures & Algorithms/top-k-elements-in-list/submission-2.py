class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap + heap
        count = Counter(nums)
        heap = []
        for num,cnt in count.items():
            heapq.heappush(heap,[cnt,num])
            if len(heap) > k: 
                heapq.heappop(heap)
        return [h[1] for h in heap]

        # bucketsort
        # count = Counter(nums)
        # freq = [[] for i in range(len(nums)+1)]

        # for num, cnt in count.items():
        #     freq[cnt].append(num)

        # ans = []
        # for i in reversed(range(len(freq))):
        #     ans.extend(freq[i])
        #     if len(ans) == k: 
        #         return ans

           