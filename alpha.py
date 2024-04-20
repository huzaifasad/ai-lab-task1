import math

def minimax(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or node_is_terminal(node):
        return evaluate(node)
    
    if maximizing_player:
        max_eval = -math.inf
        for child in generate_children(node):
            eval = minimax(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for child in generate_children(node):
            eval = minimax(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# Example functions, replace with actual implementations
def node_is_terminal(node):
    return True

def evaluate(node):
    return 0

def generate_children(node):
    return []
