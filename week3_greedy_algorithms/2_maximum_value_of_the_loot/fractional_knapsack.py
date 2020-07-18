# Uses python3
import sys
from operator import itemgetter


def get_optimal_value(capacity, weights, strengths):
    value = 0.
    strengths.sort(key=itemgetter(1), reverse=True)
    current = 0
    while capacity > 0 and current < len(weights):
        a = min(capacity, weights[strengths[current][0]])
        value += (strengths[current][1]*a)
        capacity -= a
        current += 1
    return value


if __name__ == "__main__":
    n, capacity = map(int, input().strip().split(' '))
    weights = []
    strengths = []
    for i in range(n):
        v, w = map(int, input().strip().split(" "))
        weights.append(w)
        strengths.append((i, v / w))
    opt_value = get_optimal_value(capacity, weights, strengths)
    print("{:.4f}".format(opt_value))
