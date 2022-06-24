n = int(input())

s = [".,!? ", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

for _ in range(n):
    figs = str(input())
    
    cnt, num = 0, 0
    for i in range(len(figs)):
        if figs[i] == '0':
            if num:
                print(s[num-1][(cnt-1) % len(s[num-1])], end="")
            cnt, num = 0, 0
            continue
        num = int(figs[i])
        cnt += 1
    print()