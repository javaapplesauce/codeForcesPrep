import sys

def solve():
    input = sys.stdin.readline
    
    t = int(input())
    
    for _ in range(t):
        n, s = map(int, input().split())
        
        # Suppose you read a line of input like this:
        line = input()
        nums = list(map(int, line.split()))

        minimum = min(nums)
        maximum = max(nums)
        
        if (abs(s - minimum) > abs(s - maximum)):
            min_dist = abs(s - maximum)
            max_dist = abs(s - minimum)
        else:
            min_dist = abs(s - minimum)
            max_dist = abs(s - maximum)
        
        distances = abs(maximum-minimum)
        
        print(distances + min_dist)
    
    
if __name__ == '__main__':
    solve()