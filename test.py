import random
import time

# Function to generate random and unique numbers within a range
def generate_unique_numbers(start, end, count):
    return random.sample(range(start, end + 1), count)

# Function to build a tree from a list of numbers
def build_tree(numbers):
    tree = {}
    for num in numbers:
        tree[num] = set()
    return tree

# Function to add edges between nodes in a tree
def add_edges(tree):
    nodes = list(tree.keys())
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            if random.choice([True, False]):  # Randomly add edges between nodes
                tree[nodes[i]].add(nodes[j])
                tree[nodes[j]].add(nodes[i])
    return tree

# BFS implementation
def bfs(graph, start):
    visited = set()
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            # Add adjacent vertices to queue
            queue.extend(graph[vertex] - visited)

# DFS implementation
def dfs(graph, start):
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            # Add adjacent vertices to stack
            stack.extend(graph[vertex] - visited)

# Define ranges for each set
ranges = [(1000, 4000), (40001, 80000), (80001, 200000), (200001, 1000000), (1000001, 2000000)]

# Iterate over each range
for idx, (start, end) in enumerate(ranges):
    print(f"Set {idx+1}: Range ({start}, {end})")

    # Generate unique numbers within the range
    numbers = generate_unique_numbers(start, end, 100)

    # Build tree
    tree = build_tree(numbers)

    # Add edges to the tree
    tree = add_edges(tree)

    # Measure time for BFS
    start_time = time.time()
    bfs(tree, numbers[0])
    bfs_time = time.time() - start_time

    # Measure time for DFS
    start_time = time.time()
    dfs(tree, numbers[0])
    dfs_time = time.time() - start_time

    print(f"BFS Time: {bfs_time} seconds")
    print(f"DFS Time: {dfs_time} seconds")
    print("-------------------------")
