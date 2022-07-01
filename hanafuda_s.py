while True:
    n, r = [int(_) for _ in input().split()]
    if n == 0 and r == 0:
        break
    cards = [_ for _ in range(n, 0, -1)]
    for _ in range(r):
        p, c = [int(_) for _ in input().split()]
        above = cards[:p-1]
        change = cards[p-1:p+c-1]
        not_change = cards[p+c-1:]
        cards = change+above+not_change

    print(cards[0])
