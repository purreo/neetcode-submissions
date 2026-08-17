# mistakes:
# not thinking before writing, but I am going back and fixing mistakes when I re-read my code.
# forgot to check if the stack is not empty before grabbing the top of the stack (stack[-1]). Got index out of range error.
class Solution:
    def isValid(self, s: str) -> bool:
        p_map = {']':'[', '}':'{', ')':'('}
        stack = []

        for c in s:
            print("stack: " + str(stack))
            if len(stack) > 0: # must check if stack is not empty to avoid error
                if c in p_map and stack[-1] == p_map[c]: # if c is closed and top of stack is the matching open parentheses
                    stack.pop()
                else: # c is open, so we append to stack
                    stack.append(c)
            else:
                stack.append(c) 
        return len(stack) == 0
            
            