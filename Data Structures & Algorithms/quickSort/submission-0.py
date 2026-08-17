# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quick(pairs, 0, len(pairs) - 1)
        return pairs
    def quick(self, arr, s, e) -> None:
        if e - s + 1 <= 1:
            return
        pivot = arr[e] # just for this problem. normally, pivot = sorted(pairs[s],pairs[m],pairs[e])[1]
        left = s
        # elements < than pivot on left side (normally <=)
        for i in range(s,e):
            if arr[i].key < pivot.key:
                arr[left],arr[i] = arr[i],arr[left]
                left += 1
        # move pivot in-between left & right sides
        arr[e] = arr[left]
        arr[left] = pivot
        
        # Quick sort left side
        self.quick(arr, s, left - 1)

        # Quick sort right side
        self.quick(arr, left + 1, e)