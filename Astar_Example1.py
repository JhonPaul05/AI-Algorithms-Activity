  import heapq

graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 1},
    'C': {'D': 1},
    'D': {}
}

heuristic = {
    'A': 3,
    'B': 2,
    'C': 1,
    'D': 0
}

def astar(start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))
    cost = {start: 0}
    parent = {}

    while open_list:
        current = heapq.heappop(open_list)[1]

        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.reverse()
            return path

        for neighbor, weight in graph[current].items():
            new_cost = cost[current] + weight

            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]
                heapq.heappush(open_list, (priority, neighbor))
                parent[neighbor] = current

print("Shortest Path:", astar('A','D'))
