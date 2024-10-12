from dataclasses import dataclass

class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children
    
    def add_child(self, child):
        self.children.append(child)
    
    def is_terminal(self):
        return len(self.children) == 0
    
    def evaluate(self):
        return self.value

    def children(self):
        return self.children

@dataclass
class Pair:
    node: Node
    evaluation: float

def minimax(node, depth, maximizingPlayer):
    if depth == 0 or node.is_terminal():
        return Pair(None, node.evaluate())
    value = None
    best = None
    if maximizingPlayer:
        value = float("-inf")
        for child in node.children():
            p = minimax(child, depth-1, False)
            evaluation = p.evaluation
            if evaluation > value:
                value = evaluation
                best = child
    else:
        value = float("inf")
        for child in node.children():
            p = minimax(child, depth-1, True)
            evaluation = p.evaluation
            if evaluation < value:
                value = evaluation
                best = child
    return Pair(best, value)

def negamax(node, depth, color):
    if depth == 0 or node.is_terminal():
        return Pair(None, color*node.evaluate())
    value = float("-inf")
    best = None
    for child in node.children():
        p = negamax(child, depth-1, -color)
        evaluation = -p.evaluation
        if evaluation > value:
            value = evaluation
            best = child
    return Pair(best, value)

def alphabeta(node, depth, alpha, beta, color):
    if depth == 0 or node.is_terminal():
        return Pair(None, color*node.evaluate())
    value = float("-inf")
    best = None
    for child in node.children():
        p = alphabeta(child, depth-1, -beta, -alpha, -color)
        evaluation = -p.evaluation
        if evaluation > value:
            value = evaluation
            best = child
        alpha = max(alpha, evaluation)
        if alpha >= beta:
            break
    return Pair(best, value)