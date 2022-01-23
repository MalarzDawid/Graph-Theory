class Graph:
    def __init__(self, adj_list: dict, nodes: int) -> None:
        self.adj_list = adj_list
        self.nodes = nodes
        self.visited = [False] * self.nodes

    def BFS(self, start: int) -> None:
        queue = []
        queue.append(start)

        self.visited[start] = True

        while queue:
            node = queue.pop(0)

            if node in self.adj_list:
                for adj_node in self.adj_list[node]:
                    if self.visited[adj_node] == False:
                        queue.append(adj_node)
                        self.visited[adj_node] = True
                        print(adj_node, end=" ")
        self.visited = [False] * self.nodes

    def DFS(self, start: int) -> list:
        if self.visited[start]:
            return
        self.visited[start] = True
        neighbours = self.adj_list[start]
        for neighbour in neighbours:
            self.DFS(start=neighbour)
        return self.visited

    def display(self) -> None:
        for node in self.adj_list.items():
            print(node)


if __name__ == "__main__":
    adj_list = {0: [1, 2],
                1: [0, 3, 4], 
                2: [0, 3], 
                3: [1, 2, 5], 
                4: [1], 
                5: [3]}

    g = Graph(adj_list, len(adj_list))
    print("Start Node: 0")
    g.BFS(0)
    print("\nGraph Display: ")
    g.display()
    print("DFS start: ")
    dfs_output = g.DFS(0)
    print(dfs_output)
