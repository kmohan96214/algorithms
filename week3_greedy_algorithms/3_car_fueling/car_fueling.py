# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    stops = [0] + stops + [distance]
    current = 0
    n_stops = 0
    while current < len(stops) - 1:
        now = current
        while current+1 < len(stops) and tank >= stops[current + 1] - stops[now]:
            current += 1
        if now == current:
            return -1
        n_stops += 1
    return n_stops-1


if __name__ == '__main__':
    d = int(input())
    tank = int(input())
    n_stops = int(input())
    stops = list(map(int, input().strip().split(' ')))
    print(compute_min_refills(d, tank, stops))
