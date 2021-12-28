graph = {}
with open("input") as input_file:
    for line in input_file:
        node, edge = line.strip().split("-")

        if node in graph:
            graph[node].append(edge)
        else:
            graph[node] = [edge]

        if edge in graph:
            graph[edge].append(node)
        else:
            graph[edge] = [node]


def get_paths(graph, start, end, paths=None, visited=None):
    if visited == None:
        visited = [start]
    if paths == None:
        paths = []

    next_nodes = graph[start]
    for node in next_nodes:
        if (node == node.lower()) and node in visited:
            continue
        visited.append(node)
        if node == end:
            paths.append([*visited])
        else:
            get_paths(graph, node, end, paths, visited)
        visited.reverse()
        visited.remove(node)
        visited.reverse()
    return paths


paths = get_paths(graph, "start", "end")
print(len(paths))
