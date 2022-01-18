def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fatorial(n - 1)
m = fatorial(3)
print("Fatorial de 3 são", m)

