class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # map:
            # key: alphabetical ordering of each string
            # val: each anagram list that fits the key
        # input: list of strings
        # output: list of lists, grouped by each map key
        # time: O(n*m) - O(n) to loop through each string in input, O(m) to alphabetize each string
        # space: O(n) - only dependent on input

        map = {} # initialize map of lists
        ans = []
        for s in strs:
            alpha_s = "".join(sorted(s))

            # create list for alphabetical string if not in map and add og s
            if alpha_s not in map:
                map[alpha_s] = []
            map[alpha_s].append(s)
        

        # append map value lists to ans
        for k in map:
            ans.append(map[k])

        return ans