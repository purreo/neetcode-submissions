class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i <= j:
            # move pointers, skipping all non-alphanumeric characters (including spaces).
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            # if lowercase letters are not equal, return false because string is not a palindrome.
            if s[i].lower() != s[j].lower():
                return False
            # move pointers when letters are equal    
            i += 1
            j -= 1
        return True # string is a palindrome