def BFS(graph,start):
    visited,queue = set(), [start]
    while queue :
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex]- visited)
    return visited

def BFS_Paths(graph,start,goal):
    queue = [(start,[start])]
    while queue:
        (vertex,path) = queue.pop(0)
        for next_path in graph[vertex] - set(path):
            if next_path == goal:
                yield path + [next_path]
            else:
                queue.append((next_path,path+[next_path]))
    return queue
