def newArray(length):
    return ["" for _ in range(length)]

class stack:
    def __init__(self, length):
        self.head = 0
        self.array = newArray(length)

    def push(self, userInput):
        if self.head == len(self.array):
            print("error: Stack Ss Full")
            return
        self.array[self.head] = userInput
        self.head = self.head + 1
        print("success: Value Pushed")

    def pop(self):
        if self.head == 0:
            print("error: Stack Is Empty")
            return
        self.head = self.head - 1
        popValue = self.array[self.head]
        self.array[self.head] = ""
        print("success: Value"+popValue)

mystack = stack(3)

mystack.push("hello")
print(mystack.array)
mystack.push("no")
print(mystack.array)
mystack.push("yes")
print(mystack.array)
mystack.push("maybe")
print(mystack.array)