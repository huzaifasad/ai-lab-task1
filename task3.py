import heapq

# Define heuristic function (Manhattan distance)
def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

# Get neighbors of a given node in the maze
def get_neighbors(node, maze):
    neighbors = []
    x, y = node
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Possible movements: down, up, right, left
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] != 'W':
            neighbors.append((nx, ny))
    return neighbors

# Implement A* search algorithm
def astar(maze, start, goal):
    visited = set()
    came_from = {}  # To keep track of parent nodes
    pq = []
    heapq.heappush(pq, (0, start))  # (f-value, node)
    while pq:
        f, current = heapq.heappop(pq)
        if current == goal:
            # Goal reached, reconstruct path
            path = []
            while current != start:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        if current in visited:
            continue
        visited.add(current)
        for neighbor in get_neighbors(current, maze):
            g_value = 1  # Assuming cost of movement between nodes is 1
            h_value = heuristic(neighbor, goal)
            f_value = g_value + h_value
            heapq.heappush(pq, (f_value, neighbor))
            came_from[neighbor] = current  # Update parent node
    return None  # Goal not reachable

# Define the maze
maze = [
    ['4', 'R', '3', '2', '1'],
    ['H', 'W', 'STU', 'MN', 'IJ'],
    ['XY', 'V', 'Q', 'OP', 'KL'],
    ['F', 'G', '0', '1', 'A'],
    ['BCDE', '2', '3', '4']
]

# Define start and goal nodes
start = (3, 4)
goal = (0, 0)

# Run A* search
path = astar(maze, start, goal)
print("Path:", path)
