class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node 
    
    def push_back(self, data):
        new_node = Node(data)
        temp_node = self.head
        if self.head == None:
            self.head = new_node
            return
        while temp_node.next != None:
            temp_node = temp_node.next
        temp_node.next = new_node

    def insert_index(self, index, data):
        if index > self.size():
            return None
        if index == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        elif index == self.size():
            new_node = Node(data)
            temp_node = self.head
            if self.head == None:
                self.head = new_node
                return
            while temp_node.next != None:
                temp_node = temp_node.next
            temp_node.next = new_node
        else:
            temp_node = self.head
            new_node = Node(data)
            for _ in range(index-1):
                temp_node = temp_node.next
            temp_node_2 = temp_node.next
            temp_node.next = new_node
            new_node.next = temp_node_2

    def delete_index(self, index):
        if index >= self.size():
            return None
        if index == 0:
            self.head = self.head.next
        else:
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            temp_node.next = temp_node.next.next

    def pop_front(self):
        if(self.size() == 0):
            return
        self.head = self.head.next
    
    def pop_back(self):
        temp_node = self.head
        if self.size() == 0:
            return            
        if self.size()==1:
            self.head = None
            return
        for _ in range(self.size()-2):
            temp_node = temp_node.next
        temp_node.next = None
    
    def get(self, index):
        if index > self.size()-1 or index < 0:
            return -1
        temp_node = self.head
        for _ in range(index):
            temp_node = temp_node.next
        return temp_node.data

    def size(self):
        temp_node = self.head
        count = 0
        while temp_node != None:
            count += 1
            temp_node = temp_node.next
        return count
    

    def print_list(self):
        temp_node = self.head
        while temp_node != None:
            print(temp_node.data, end=" -> ")
            temp_node = temp_node.next
        print()

my_linked_list = LinkedList()

my_linked_list.push_front(7)
my_linked_list.push_front(2)
my_linked_list.push_front(1)
my_linked_list.insert_index(3,0)
my_linked_list.print_list()
# my_linked_list.delete_index(2)
# my_linked_list.push_front(6)
# my_linked_list.push_back(4)
# my_linked_list.print_list()
# print(my_linked_list.get(4))
# print("fin")