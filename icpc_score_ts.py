while True:
    n = int(input())
    if n == 0:
        break

    score = [int(input()) for _ in range(n)]

    score.sort()
    print(sum(score[1:n-1]) // (n-2))
