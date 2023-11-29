def newArray(length):
    return ["" for _ in range(length)]


class queue:
    def __init__(self, length): # public function new()
        self.head = 0
        self.tail = 0
        self.numOfItem = 0
        self.list =  newArray(length) # creates an array of length 


    def enqueue(self, userInput): # public funciton enqueue 
        if self.numOfItem == len(self.list):
            print("error: list is full")
            return

        self.list[self.tail] = userInput
        self.tail = (self.tail+1) % len(self.list)
        self.numOfItem += 1
        print("success: input added")
        return


    def dequeue(self): # public funciton dequeue
        if self.numOfItem == 0:
            print("error: list is empty")
            return ""
        
        theValue = self.list[self.head]
        self.list[self.head] = ""
        self.head= (self.head+1) % len(self.list)
        self.numOfItem -= 1
        print("success: got the value: "+theValue)
        return theValue