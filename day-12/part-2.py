from collections import Counter

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


def can_visit(visited, node):
    has_visited = node in visited
    if not has_visited:
        return True
    if node == "end" or node == "start":
        return False
    elif node == node.upper():
        return True
    else:
        lowercase_nodes = [node for node in visited if node.lower() == node]
        c = Counter(lowercase_nodes)
        lowercase_count = max([v for k, v in c.items()])
        return lowercase_count < 2


def get_paths(graph, start, end, paths=None, visited=None):
    if visited == None:
        visited = [start]
    if paths == None:
        paths = []

    next_nodes = graph[start]
    for node in next_nodes:
        if not can_visit(visited, node):
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
