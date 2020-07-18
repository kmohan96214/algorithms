# python3


def max_pairwise_product(numbers):
    max1, max2 = 0, 0
    for i in numbers:
        if i >= max1:
            max1, max2 = i, max1
        elif i>=max2:
            max2 = i            
    return max1 * max2


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
