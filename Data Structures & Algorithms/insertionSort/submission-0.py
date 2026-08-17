# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        n = len(pairs)
        states = [] # should be = to len(pairs)

        for i in range(n):
            j = i-1
            # while j in bounds and pairs can swap
            while j >= 0 and pairs[j].key > pairs[j+1].key:
                # swap smaller with larger
                pairs[j], pairs[j+1] = pairs[j+1], pairs[j]
                j -= 1
            states.append(pairs[:])
        return states