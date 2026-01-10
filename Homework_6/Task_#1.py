def has_path(graph, start, end):
    visited = set()
    stack = [start]
    while stack:
        current = stack.pop()
        if current == end:
            return True
        if current in visited:
            continue
        visited.add(current)
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                stack.append(neighbor)
    return False
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": ["F"],
    "F": []
}
print(has_path(graph, "A", "E"))
print(has_path(graph, "A", "F"))
print(has_path(graph, "C", "D"))
print(has_path(graph, "B", "D"))
print(has_path(graph, "D", "A"))
