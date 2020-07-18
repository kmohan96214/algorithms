# Uses python3
import sys


def get_change(m):
    coin_types = [10, 5, 1]
    # write your code here
    coins, current = 0, 0
    while m > 0 and current < len(coin_types):
        if m >= coin_types[current]:
            coins += (m // coin_types[current])
            m %= coin_types[current]
        current += 1
    return coins


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
