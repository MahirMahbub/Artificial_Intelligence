from math import log2
from typing import List


def mini_max(depth: int, node: int, min_max_check: bool, values: List[int], tree_height: int, alpha: float,
             beta: float):
    if depth == tree_height:
        return values[node]
    if min_max_check:
        best: float = float("-inf")
        for i in range(2):
            best = max(best, mini_max(depth + 1, node * 2+i, False, values, tree_height, alpha, beta))
            alpha = max(best, alpha)
            if beta <= alpha:
                break
        return best
    else:
        best: float = float("inf")
        for i in range(2):
            best = min(best, mini_max(depth + 1, node * 2 + i, True, values, tree_height, alpha, beta))
            beta = min(best, beta)
            if beta <= alpha:
                break
        return best


scores: List[int] = [3, 5, 2, 9, 12, 5, 23, 23]
length_score: int = len(scores)
height: int = log2(length_score)
result: int = mini_max(0, 0, True, scores, height, float("-inf"), float("inf"))
print(result)
