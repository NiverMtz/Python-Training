def contar_primos(n):
    cuenta = 0

    for i in range(2, n + 1):
        if i > 1:
            for j in range(2, i):
                if (i % j) == 0:
                    break
            else:
                cuenta += 1
    return cuenta


primos = contar_primos(13)
print(primos)
