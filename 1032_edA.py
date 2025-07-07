import sys


def solve():
    input = sys.stdin.readline
    
    t = int(input())
    
    for _ in range(t):
        
        a, x, y = map(int, input().split())
        
        if ((x > a and y > a ) or (a > x and a > y)):
            print("YES")
        else: 
            print("NO")


if __name__ == '__main__':
    solve()