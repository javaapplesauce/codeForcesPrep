import sys
import math

def solve():
    input = sys.stdin.readline
    t = int(input())
    5
    for x in range(t):
        
        alen = int(input())
        x1, y1, x2, y2 = map(int, input().split())
        
        a = []
        while len(a) < alen:
            a.extend(map(float, input().split()))

        
        a.append(math.hypot(x1 - x2, y1 - y2))
        m = max(a)
        
        asum = sum(a)
        
        if (m <= (asum - m)):
            print("YES")
        else:
            print("NO")
        
        



if __name__ == '__main__':
    solve()