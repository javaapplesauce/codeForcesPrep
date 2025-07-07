import sys
import math



def solve():
    input = sys.stdin.readline
    
    t = int(input())
    
    for _ in range(t):
        
        k, a, b, x, y = map(int, input().split())
        n = 0
        
        # 1) Cook A first (requirement a, drop x), then B (requirement b, drop y)
        if (a <= k):
            n_a = (k - a) // x + 1
        else:
            n_a = 0
        remainder_a = k - (n_a * x)
        if (b <= remainder_a):
            n_a += (remainder_a - b) // y + 1
        else:
            n_a += 0
            
        if (b <= k):
            n_b = (k - b) // y + 1
        else:
            n_b = 0
        remainder_b = k - (n_b * y)
        if (a <= remainder_b):
            n_b += (remainder_b - a) // x + 1
        else:
            n_b += 0
            
        print(max(n_a, n_b))

        
if __name__ == '__main__':
    solve()