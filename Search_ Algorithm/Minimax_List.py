from math import log2
from typing import List


def mini_max(depth: int, node: int, min_max_check: bool, values: List[int], tree_height: int):
    if depth == tree_height:
        return values[node]
    if min_max_check:
        return max(mini_max(depth + 1, node * 2, False, values, tree_height),
                   mini_max(depth + 1, node * 2 + 1, False, values, tree_height))
    else:
        return min(mini_max(depth + 1, node * 2, True, values, tree_height),
                   mini_max(depth + 1, node * 2 + 1, True, values, tree_height))


scores: List[int] = [3, 5, 2, 9, 12, 5, 23, 23]
length_score: int = len(scores)
height: int = log2(length_score)
result: int = mini_max(0, 0, True, scores, height)
print(result)
