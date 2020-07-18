# Uses python3
from operator import itemgetter
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')



def optimal_points(segments):
    points = []
    # write your code here
    segments.sort(key=itemgetter(1))
    curr = segments[0][1]
    points.append(curr)

    for i in range(1, len(segments)):
        if curr < segments[i][0] or curr > segments[i][1]:
            curr = segments[i][1]
            points.append(curr)
    return points


if __name__ == '__main__':
    n = int(input())
    segments = []
    for i in range(n):
        x, y = map(int, input().strip().split(" "))
        segments.append(Segment(x, y))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
