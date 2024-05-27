numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]  # 1
primes = []
not_primes = []
is_prime = True
for i in range(2, 15 + 1):
    for j in range(2, round(i ** 0.5) + 1):
        (f'{i} : {j} = {i % j}')
        if i % j == 0:
            not_primes.append(i)
            break
    else:
        primes.append(i)

print(not_primes)
print(primes)















