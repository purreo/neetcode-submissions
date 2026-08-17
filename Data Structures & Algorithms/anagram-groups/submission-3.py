class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # map:
            # key: alphabetical ordering of each string
            # val: each anagram list that fits the key
        # input: list of strings
        # output: list of lists, grouped by each map key
        # time: O(n*m) - O(n) to loop through each string in input, O(m) to alphabetize each string
        # space: O(n) - only dependent on input

        ap = defaultdict(list) # initialize map of lists
        for s in strs:
            key = "".join(sorted(s)) # create map key as sorted string
            ap[key].append(s)
            # map value at key is either the key that already exists or 
            # default val of an empty list since it's a new key
            # then add the new string to that map value
        return list(ap.values())
