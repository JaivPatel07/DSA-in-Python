class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")


if __name__ == "__main__":

    def nextGreaterElement(nums):
        stack = Stack()
        n = len(nums)
        ans = [-1] * n

        for i in range(n - 1, -1, -1):
            while not stack.is_empty() and stack.peek() <= nums[i]:
                stack.pop()

            if not stack.is_empty():
                ans[i] = stack.peek()

            stack.push(nums[i])

        return ans
            
        



