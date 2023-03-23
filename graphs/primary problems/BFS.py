from queue import SimpleQueue


def bfs(graph,s):
    queue = SimpleQueue()
    visited = [False]*len(graph)
    queue.put(s)
    visited[s] = True
    while not queue.empty():
        u = queue.get()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.put(v)
                