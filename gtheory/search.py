def dfs(visited, graph, at):
    if visited[at]:
        return
    visited[at] = True

    for neighbour in graph[at]:
        dfs(visited, graph, neighbour)
    return visited


if __name__ == "__main__":
    graph = [[1, 2], [0, 3, 4], [0], [1], [2, 3]]
    visited = [False, False, False, False, False]
    output = dfs(visited, graph, 0)
    print(output)
