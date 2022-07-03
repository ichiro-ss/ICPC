tri_n = 182
lim = 10 ** 6 + 1
INF = 10 ** 9

pollock = [0] * tri_n
p_odd = pollock.copy()

for i in range(1, tri_n):
    x = i * (i+1) * (i+2) // 6
    pollock[i] = x
    if x & 1:
        p_odd[i] = x

dp = [_ for _ in range(lim)]
dp_odd = [_ for _ in range(lim)]

for i in range(lim):
    for j in range(tri_n):
        if i - pollock[j] < 0:
            break
        dp[i] = min(dp[i-pollock[j]]+1, dp[i])
        if j & 1:
            dp_odd[i] = min(dp_odd[i-p_odd[j]]+1, dp_odd[i])

while True:
    fig = int(input())
    if not fig:
        break
    print(dp[fig], dp_odd[fig])
