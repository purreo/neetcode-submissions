class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1 <= nums.length <= 10^4. - greedy, 2 ptrs, heap, dp
        # k = heap - O(nlogn), 2ptrs O(n)
        # count freqs of each element and then use heap of size k to get the most frequent
        # time: O(nlogn), space: O(k) (-1000 to 1000 in hashmap, k in heap)

        # for each num in nums: count the freq

        # for each num in freq map:
            # add to heap to get kth most frequent after popping
            # if len(heap) > k, pop from the heap

        # return list of heap values[:k]

        freq = Counter(nums)
        heap = []
        # need to store count on the heap too
        for num, count in freq.items():
            heapq.heappush(heap,[count,num])
            if len(heap) > k:
                heapq.heappop(heap)
        
        ans = []
        for count,num in heap:
            ans.append(num)
        return ans
        
