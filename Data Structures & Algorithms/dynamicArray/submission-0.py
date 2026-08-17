class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [None] * self.capacity
        self.size = 0

    def get(self, i: int) -> int:
        print("get: ",i , " element: ", self.arr[i])
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        if self.arr[i] is None: # number didn't exist in spot before
            self.size += 1
            print("increment size: ",self.size)
        self.arr[i] = n
        print("position: ", i, " set to: ", self.arr[i])

    def pushback(self, n: int) -> None:
        print("old last elem: ", self.arr[self.size-1])
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size += 1
        print("last element is: ", self.arr[self.size-1])
    def popback(self) -> int:
        last = self.arr[self.size-1]
        self.arr[self.size-1] = None
        self.size -= 1
        print("popped: ",last)
        return last

    def resize(self) -> None:
        self.arr.extend([None] * self.capacity)
        self.capacity *= 2
        print("resized arr: ",self.arr)

    def getSize(self) -> int:
        print("size: ",self.size, " arr: ",self.arr)
        return self.size
    
    def getCapacity(self) -> int:
        print("capacity: ",self.capacity, " arr: ",self.arr)
        return self.capacity
