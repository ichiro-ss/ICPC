cnt = 0
dh = [1, 0, -1, 0]
dw = [0, 1, 0, -1]

def dfs(pr_h, pr_w, passed, tiles):
    global cnt
    if tiles[pr_h][pr_w] == '#':
        return
        
    passed[pr_h][pr_w] = True
    cnt += 1
    for i in range(4):
        nx_h, nx_w = pr_h+dh[i], pr_w+dw[i]
        if 0 <= nx_h < h and 0 <= nx_w < w\
            and not passed[nx_h][nx_w]:
            dfs(nx_h, nx_w, passed, tiles)

while True:
    w, h = [int(_) for _ in input().split()]
    cnt = 0
    if w == 0 and h == 0:
        break
    tiles = [[] for _ in range(h)]
    for i in range(h):
        tiles[i] = [str(_) for _ in list(input())]
    ph, pw = 0, 0
    for i in range(h):
        for j in range(w):
            if tiles[i][j] == '@':
                ph, pw = i, j
    passed = [[False for i in range(w)] for j in range(h)]
    dfs(ph, pw, passed, tiles)
    print(cnt)
    