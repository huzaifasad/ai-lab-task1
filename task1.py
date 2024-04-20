import numpy as np
import time
import pandas as pd
import matplotlib.pyplot as plt

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def generate_unique_numbers(start, end, count):
    return np.random.choice(np.arange(start, end + 1), count, replace=False)

def build_tree(numbers):
    root = TreeNode(numbers[0])
    for num in numbers[1:]:
        node = TreeNode(num)
        parent = root
        while True:
            if num < parent.value:
                if parent.children:
                    parent = parent.children[0]
                else:
                    parent.children.append(node)
                    break
            else:
                if parent.children:
                    parent = parent.children[-1]
                else:
                    parent.children.append(node)
                    break
    return root

def bfs(root, goal):
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.value == goal:
            return True
        queue.extend(node.children)
    return False

def dfs(root, goal):
    stack = [root]
    while stack:
        node = stack.pop()
        if node.value == goal:
            return True
        stack.extend(node.children[::-1])
    return False

# Generate random and unique numbers for each range
ranges = [1000, 40000, 80000, 200000, 1000000]
tree_sizes = []
bfs_times = []
dfs_times = []

for size in ranges:
    numbers = generate_unique_numbers(1, size, size)
    tree = build_tree(numbers)
    tree_sizes.append(size)
    
    start_time = time.time()
    bfs(tree, size - 220)
    bfs_time = time.time() - start_time
    bfs_times.append(bfs_time)
    
    start_time = time.time()
    dfs(tree, size - 220)
    dfs_time = time.time() - start_time
    dfs_times.append(dfs_time)

# Create a DataFrame to store the results
results = pd.DataFrame({
    'Tree Size': tree_sizes,
    'BFS Time': bfs_times,
    'DFS Time': dfs_times
})

# Plot a bar chart
plt.bar(results['Tree Size'], results['BFS Time'], color='blue', label='BFS Time')
plt.bar(results['Tree Size'], results['DFS Time'], color='red', label='DFS Time', alpha=0.5)
plt.xlabel('Tree Size')
plt.ylabel('Time (seconds)')
plt.title('Time taken by BFS and DFS for different tree sizes')
plt.legend()
plt.show()

print(results)
