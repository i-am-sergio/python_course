class Graph:
    def __init__(self):
        self.__adyacency_list = {}
        self.__num_edges = 0
    
    def insert_node(self, node):
        if node not in self.__adyacency_list:
            self.__adyacency_list[node] = []

    def insert_edge(self, node1, node2):
        if node1 in self.__adyacency_list and node2 in self.__adyacency_list:
            self.__adyacency_list[node1].append(node2)
            self.__adyacency_list[node2].append(node1)
        self.__num_edges += 1

    def get_num_nodes(self) -> int:
        return len(self.__adyacency_list)

    def get_num_edges(self) -> int:
        return self.__num_edges
    
    def print_graph(self):
        for node, adyacentes in self.__adyacency_list.items():
            print(node, " -> ", adyacentes)
    

