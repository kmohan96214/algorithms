# Uses python3

def max_dot_product(a, b):
    # write your code here
    a.sort()
    b.sort()
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().strip().split(" ")))
    b = list(map(int, input().strip().split(" ")))
    print(max_dot_product(a, b))
