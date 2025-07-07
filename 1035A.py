import sys

def solve():
    input = sys.stdin.readline

    t = int(input())

    for x in range (t):
        
        a, b, x, y = map(int, input().split())
        total = 0

        if ((a > b) & (a % 2 == 0)) | ((a > (b+1)) & (a % 2 == 1)):
            total = -1
        elif ((a == (b+1)) & a % 2 == 1):
            total = y
        else:
            while (a < b):
                if (a % 2 == 1):
                    total += x
                    a += 1
                else:
                    total += min(x, y)
                    a += 1
        print(total)
                    
            
    




if __name__ == '__main__':
    solve()