class Queue:
    def __init__(self,size):
        self.size=size
        self.queue=[None]*self.size
        self.rear=-1
        self.front=0
    def isempty(self):
        if self.rear==-1 or self.front==self.size-1:
            return True
        return False
    def isFull(self):
        if self.rear==self.size-1:
            return True
        return False
    def enqueue(self,data):
        if self.isFull():
            print('The queue is full !!')
            return
        self.rear=self.rear+1
        self.queue[self.rear]=data
        print('Enqueue Done !!')
    def deque(self):
        if self.isempty():
            print('The Queue is empty !!')
        self.queue[self.front]=None
        self.front=self.front+1
        print('Dequeue Done !!')
        
    def show(self):
        return self.queue