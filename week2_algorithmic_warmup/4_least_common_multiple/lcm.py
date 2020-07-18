# Uses python3
import sys
sys.setrecursionlimit(3000)

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def gcd(a,b):
    if (b == 0):
        return a
    return gcd(b, a % b)

def lcm(a,b):
    gd = gcd(a,b)
    return (a*b)//gd

if __name__ == '__main__':
    a, b = map(int, input().split())
    # print(lcm_naive(a, b))
    print(lcm(a,b))

