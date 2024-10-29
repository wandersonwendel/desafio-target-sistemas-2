def pertence_fibonacci(numero):
    if numero < 0:
        return f"O número {numero} NÃO pertence à sequência de Fibonacci."

    a, b = 0, 1
    sequencia = [a]  # Armazenar a sequência
    
    # Gerar e armazenar os valores
    while a < numero:
        a, b = b, a + b
        sequencia.append(a)
    
    # Verifica se o valor atual é igual ao número informado
    if numero in sequencia:
        return f"O número {numero} pertence à sequência de Fibonacci.\nSequência até {numero}: {sequencia}"
    else:
        return f"O número {numero} NÃO pertence à sequência de Fibonacci.\nSequência até {numero}: {sequencia}"

# Teste com um número específico
numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
print(pertence_fibonacci(numero))
