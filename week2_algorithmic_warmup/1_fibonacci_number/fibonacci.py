# Uses python3
def calc_fib(n): 
    prev = 0
    curr = 1
    if n <=1: 
        return n
    else: 
        for i in range(2,n+1): 
            nxt = prev + curr 
            prev = curr 
            curr = nxt 
        return curr

n = int(input())
print(calc_fib(n))
