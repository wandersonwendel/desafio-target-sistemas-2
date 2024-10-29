def identificar_interruptores():
    # Estado dos interruptores e lâmpadas
    interruptores = ["A", "B", "C"]  # Nomes dos interruptores
    lampadas = ["A", "B", "C"]  # Nomes das lâmpadas
    estados_lampadas = ["apagada", "apagada", "apagada"]  # Estados iniciais das lâmpadas
    temperaturas = ["fria", "fria", "fria"]  # Temperaturas iniciais das lâmpadas

    # Passo 1: Liga o primeiro interruptor (A)
    estados_lampadas[0] = "acesa"
    temperaturas[0] = "quente"  # Lâmpada A esquenta

    # Espera (simulação, não faz nada aqui)
    # Passo 2: Desliga o primeiro interruptor e liga o segundo interruptor (B)
    estados_lampadas[0] = "apagada"  # Agora a lâmpada A está apagada
    estados_lampadas[1] = "acesa"  # A lâmpada B está acesa
    temperaturas[1] = "quente"  # Lâmpada B esquenta

    # Vamos até a sala das lâmpadas e verificamos os estados
    print("Verificando as lâmpadas:")
    for i in range(len(lampadas)):
        print(f"Lâmpada {lampadas[i]}: {estados_lampadas[i]}, Temperatura: {temperaturas[i]}")

    # Identificando quais interruptores controlam quais lâmpadas
    resultados = {}
    for i in range(len(interruptores)):
        if estados_lampadas[i] == "acesa":
            resultados[interruptores[i]] = f"Lâmpada {lampadas[i]} (Acesa)"
        elif temperaturas[i] == "quente":
            resultados[interruptores[i]] = f"Lâmpada {lampadas[i]} (Apagada, Quente)"
        else:
            resultados[interruptores[i]] = f"Lâmpada {lampadas[i]} (Apagada, Fria)"

    print("\nResultados:")
    for interruptor, lampada in resultados.items():
        print(f"Interruptor {interruptor} controla: {lampada}")

# Chamada da função para executar a simulação
identificar_interruptores()
