import sys
sys.setrecursionlimit(10 ** 9)

dh = [1, 0, -1, 0, 1, -1, 1, -1]
dw = [0, 1, 0, -1, 1, 1, -1, -1]

def dfs(c, cur_h, cur_w):
    global passed
    passed[cur_h][cur_w] = True

    for i in range(8):
        nx_h, nx_w = cur_h + dh[i], cur_w + dw[i]
        if 0 <= nx_h < h and 0 <= nx_w < w and \
            not passed[nx_h][nx_w] and c[nx_h][nx_w]:
            dfs(c, nx_h, nx_w)

def solve(c, h, w):
    global passed
    ans = 0
    for i in range(h):
        for j in range(w):
            if c[i][j] and not passed[i][j]:
                dfs(c, i, j)
                ans += 1
    return ans


while True:
    w, h = [int(_) for _ in input().split()]
    if not w and not h:
        exit()
    c = [[] for _ in range(h)]
    for i in range(h):
        c[i] = [int(_) for _ in input().split()]
    
    passed = [[False for _ in range(w)] for _ in range(h)]
    print(solve(c, h, w))
