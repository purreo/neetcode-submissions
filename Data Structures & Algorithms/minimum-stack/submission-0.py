# mistakes
# did not account for how to get tuple val when writing code, but fixed as i was stepping through. you can get it like this: tuple[i][j] where i is the position of the tuple in the list, and j is the position of the value within the tuple that you want.
# the min_stack is like a snapshot in time for the "real" stack. when i remove an element, even if it's not the min, i have to pop it from the min_stack. otherwise the indices won't be the same.
# sys_max() isn't valid for finding the max int. it's fine since i don't even need the min in its own variable.
# forgot to put self. in front of all variable names since they aren't defined in each function. they are global variables. this caused a "min_stack is not defined" error.
# "MinStack has no attribute 'min_stack'". I have put self. in front of variables in the init function too.
# ---
# self.min_stack.append(val, self.i)
# TypeError: list.append() takes exactly one argument (2 given)
# ---
# for this error, i should create the tuple object to insert in its own variable, then put it in the append statement.
# kept typing stack.push() instead of stack.append(). because the stack is actually a list, there is no push(). i know this, i just wasn't thorough when reviewing my code.
class MinStack:

    def __init__(self):
        self.i = 0
        self.stack = []
        self.min_stack = []
        
    def push(self, val: int) -> None:
        print("______push_______")
        print("self.min_stack: " + str(self.min_stack))
        print("self.stack: " + str(self.stack))
        print("self.i: " + str(self.i))
        val_tuple = (val, self.i)
        if len(self.min_stack) > 0:
            if val < self.min_stack[-1][0]: # push smaller value as new min
                self.min_stack.append(val_tuple)
            else: # push top of min_stack again
                self.min_stack.append(self.min_stack[-1])
        # stack is empty, so push (val,i) to self.min_stack
        else:
            self.min_stack.append(val_tuple)
        self.stack.append(val_tuple) # always push to stack regardless
        self.i += 1 # increment i when adding element
        print("self.stack: " + str(self.stack))
        print("self.min_stack: " + str(self.min_stack))
        print("self.i: " + str(self.i))
    # these will always be called on non-empty stacks, so i don't have to check if it's empty, but in the future, i should.
    def pop(self) -> None:
        print("______pop_______")
        print("self.min_stack: " + str(self.min_stack))
        print("self.stack: " + str(self.stack))
        print("self.i: " + str(self.i))
        self.min_stack.pop()
        self.stack.pop()
        self.i -= 1 # decrement i when removing an element
        print("self.min_stack: " + str(self.min_stack))
        print("self.stack: " + str(self.stack))
        print("self.i: " + str(self.i))

    def top(self) -> int:
        print("______top_______")
        return self.stack[-1][0]

    def getMin(self) -> int:
        print("______get_min_______")
        return self.min_stack[-1][0]
        
