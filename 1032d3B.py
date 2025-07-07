import sys


def solve():
    input = sys.stdin.readline()
    
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        lst = input().split()
        
        if (lst[0] == lst[n-1]):
            all_but_last = lst[:-1]
            if len(lst) == len(set(lst)):
                print("no")
            else:
                print("yes")       
        else:
            if len(lst) == len(set(lst)):
                print("no")
            else:
                print("yes")    

            
            
if __name__ == '__main__':
    solve()