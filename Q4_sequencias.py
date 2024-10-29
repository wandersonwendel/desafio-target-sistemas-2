def proximo_elemento_a():
    sequencia = [1, 3, 5, 7]
    print(f"{sequencia} _")
    proximo = sequencia[-1] + 2
    return sequencia + [proximo]

print("Lógica do item (a): Sequência de números ímpares, incremento de +2.")
print("Sequência a:", proximo_elemento_a())
print()


def proximo_elemento_b():
    sequencia = [2, 4, 8, 16, 32, 64]
    print(f"{sequencia} _")
    proximo = sequencia[-1] * 2
    return sequencia + [proximo]
print("Lógica do item (b): Sequência de potências de 2 (2^1, 2^2, 2^3, ...).")
print("Sequência b:", proximo_elemento_b())
print()



def proximo_elemento_c():
    sequencia = [0, 1, 4, 9, 16, 25, 36]
    print(f"{sequencia} _")
    n = len(sequencia)
    proximo = n ** 2
    return sequencia + [proximo]
print("Lógica do item (c): Sequência de quadrados perfeitos (0^2, 1^2, 2^2, ...).")
print("Sequência c:", proximo_elemento_c())
print()


def proximo_elemento_d():
    sequencia = [4, 16, 36, 64]
    print(f"{sequencia} _")
    n = 2 * (len(sequencia) + 1)
    proximo = n ** 2
    return sequencia + [proximo]
print("Lógica do item (d): Sequência de quadrados de números pares (2^2, 4^2, 6^2, ...).")
print("Sequência d:", proximo_elemento_d())
print()


def proximo_elemento_e():
    sequencia = [1, 1, 2, 3, 5, 8]
    print(f"{sequencia} _")
    proximo = sequencia[-1] + sequencia[-2]
    return sequencia + [proximo]
print("Lógica do item (e): Sequência de Fibonacci.")
print("Sequência e:", proximo_elemento_e())
print()


def proximo_elemento_f():
    sequencia = [2, 10, 12, 16, 17, 18, 19]
    print(f"{sequencia} _")
    proximo = 20
    return sequencia + [proximo]
print("Lógica do item (f): Sequência de números começando com 2, 10, e depois alternando pares e números consecutivos.")
print("Sequência f:", proximo_elemento_f())
print()
