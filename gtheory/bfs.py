
n = 4
graph = [[0, 1, 1, 0],
         [1, 0, 1, 0],
         [1, 1, 0, 1],
         [0, 0, 1, 0]]

def reconstructPath(s, e, prev):
    path = []
    at = e
    while at != None:
        at = prev[at]
        path.append(at)
    path.reverse()

    if path[0] == s:
        return path
    return 0

def solve(s):
    q = []
    q.append(s)

    visited = [False] * n
    visited[s] = True

    prev = [None] * n

    while len(q) != 0:
        node = q.pop(0)
        neighbours = graph[node]

        for i in range(1, len(neighbours)):
            next_ = neighbours[i]
            if visited[next_] == False:
                q.append(next_)
                visited[next_] = True
                prev[next_] = node
    return prev


def bfs(s, e):
    prev = solve(s)
    print("Prev; ", prev)
    return reconstructPath(s, e, prev)

a = bfs(0, 3)
print(a)