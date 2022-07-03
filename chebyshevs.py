lim_n = 123456
def eratosthenes_sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, n + 1):
        if is_prime[i]:
            for j in range(2 * i, n + 1, i):
                is_prime[j] = False
    return is_prime

is_prime = eratosthenes_sieve(lim_n * 2 + 1)
sum_prime = [0] * (lim_n * 2 + 1)

for i in range(1, lim_n * 2 + 1):
    sum_prime[i] = sum_prime[i-1]
    if is_prime[i]:
        sum_prime[i] += 1

while True:
    n = int(input())
    if not n:
        break
    print(sum_prime[n * 2] - sum_prime[n])
