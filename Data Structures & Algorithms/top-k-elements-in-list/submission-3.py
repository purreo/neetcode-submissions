class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap + heap
        # bucket sort due to the constraints: -1000 <= nums[i] <= 1000 = 2001 buckets, bound by n because there can only be at most n occurences of any num in an array (if arr len == 1)
        count = Counter(nums)
        # list of nums with a given frequency
        freq = [[] for i in range(len(nums)+1)] # +1 for 0 frequency to n freq (since loop normally stops at n-1)

        for num, cnt in count.items():
            freq[cnt].append(num)

        # iterate through freq in reverse to find k most frequent
        res = []
        for i in reversed(range(len(freq))):
            res.extend(freq[i])
            if len(res) == k:
                return res