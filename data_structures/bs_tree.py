class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

class BSTree:
    def __init__(self) -> None:
        self.root = None

    def insert_i(self, data) -> None:
        if self.root == None:
            self.root = Node(data)
        else:
            temp = self.root
            prev = None
            while temp!=None:
                prev = temp
                if data == temp.data:
                    return
                if data < temp.data:
                    temp = temp.left
                elif data > temp.data:
                    temp = temp.right
            if data < prev.data:
                prev.left = Node(data)
            elif data > prev.data:
                prev.right = Node(data)

    def __insert_r(self, root : Node, data) -> Node | None:
        if root == None:
            return Node(data)
        if data == root.data:
            return root
        if data < root.data:
            root.left = self.__insert_r(root.left, data)
        else:
            root.right = self.__insert_r(root.right, data)
        return root
    
    def insert_r(self, data):
        self.root = self.__insert_r(self.root,data)

    def find_i(self, data) -> bool:
        if self.root.data == data:
            return True
        else:
            temp = self.root
            while temp != None:
                if data == temp.data:
                    return True
                if data < temp.data:
                    temp = temp.left
                else:
                    temp = temp.right
        return False

    def __find_r(self, root :Node, data) -> bool:
        if root == None:
            return False
        if data == root.data:
            return True
        elif data < root.data:
            return self.__find_r(root.left, data)
        else:
            return self.__find_r(root.right, data)

    def find_r(self, data) -> bool:
        return self.__find_r(self.root, data)

    def delete(self, data) -> None:
        current = self.root
        if current == None:
            return
        prev = None
        while current is not None and data != current.data:
            prev = current
            current = current.left if data < current.data else current.right
        if current == None:
            return
        if prev == None: # if prev is root
            print("case: delete when is root")
            self.__delete_two_sons(current)
        else:
            if current.left and current.right:
                self.__delete_two_sons(current)
                print("case: delete when has two sons")
            elif not current.left and not current.right:
                self.__delete_leaf(current, prev)
                print("case: delete when is leaf")
            else:
                self.__delete_one_son(current, prev)
                print("case: delete when has one son")
                
    def __delete_leaf(self, current :Node, father :Node) -> None:
        if current.data < father.data:
            father.left = None
        else:
            father.right = None
        del current

    def __delete_one_son(self, current :Node, father :Node) -> None:
        temp = current
        if temp.left != None:
            if temp.data < father.data:
                father.left = temp.left
            else:
                father.right = temp.left
        else:
            if temp.data < father.data:
                father.left = temp.right
            else:
                father.right = temp.right

    def __delete_two_sons(self, current: Node) -> None:
        father = current
        successor = current.right
        # Encontrar el nodo sucesor inorder
        while successor.left:
            father = successor
            successor = successor.left

        current.data = successor.data
        self.__delete_one_son(successor, father)
        
    def inorder(self, root: Node) -> None:
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def preorder(self, root: Node) -> None:
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root: Node) -> None:
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

    def print_iter(self) -> None:
        stack = []
        current = self.root
        while len(stack)!=0 or current != None:
            if current:
                stack.insert(0,current)
                current = current.left
            else:
                current = stack[0]
                stack.pop(0)
                print(current.data, end=" ")
                current = current.right
        print()

    def print_tree(self, order:str = "iter") -> None:
        print(order+"orden", end=": ")
        if order == "in":
            self.inorder(self.root)
        elif order == "pre":
            self.preorder(self.root)
        elif order == "post":
            self.postorder(self.root)
        else:
            self.print_iter() 
        print()

    def __graph_tree(self, node, depth):
        if node:
            self.__graph_tree(node.right, depth + 1)
            print("  " * depth + str(node.data))
            self.__graph_tree(node.left, depth + 1)

    def graph_tree(self):
        self.__graph_tree(self.root, 0)

    def __graph_tree_2(self, node, prefix="", is_left=True):
        if node is not None:
            print(prefix + ("|-- " if is_left else "`-- ") + str(node.data))
            self.__graph_tree_2(node.left, prefix + ("|   " if is_left else "    "), True)
            self.__graph_tree_2(node.right, prefix + ("|   " if is_left else "    "), False)

    def graph_tree_2(self):
        self.__graph_tree_2(self.root)

    def __get_height_r(self, temp : Node):
        if temp == None:
            return 0
        else:
            height_left = self.__get_height_r(temp.left)
            height_right = self.__get_height_r(temp.right)
            return height_left+1 if height_left > height_right else height_right+1
    
    def get_height_r(self):
        return self.__get_height_r(self.root)

    def get_height(self):
        height = 0
        queue = []
        queue.append(self.root)
        queue.append(None)
        while len(queue) != 0:
            temp = queue[0]
            queue.pop(0)
            if temp == None:
                height +=1
            if temp:
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            elif len(queue) != 0:
                queue.append(None)
        return height

"""
                30
    15                         90
8       21          36                98
                33         71
                         56    72
                       50
                        51
"""
bstree = BSTree()
nodos = [30,15,90,8,21,36,98,33,71,56,72,50,51]
for num in nodos:
    bstree.insert_r(num)

bstree.print_tree("in")
bstree.print_tree("pre")
bstree.print_tree("post")
bstree.graph_tree_2()
print(bstree.get_height_r())
print(bstree.get_height())

delete_nodos = [51,90,71,30,21,8,36,56,33,72,15,50]
for num in delete_nodos:
    bstree.delete(num)

bstree.print_tree("in")