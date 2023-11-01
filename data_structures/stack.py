class Stack:
    def __init__(self):
        self.__elements = []

    def push(self,element: int):
        self.__elements.append(element)
    
    def pop(self):
        if not self.empty():
            self.__elements.pop()
        else:
            print("Stack is empty")
    
    def top(self):
        if not self.empty():
            return self.__elements[self.size()-1]

    def empty(self):
        return len(self.__elements)==0 
    
    def size(self):
        return len(self.__elements)


