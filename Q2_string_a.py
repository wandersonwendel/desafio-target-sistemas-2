def contar_letra_a(texto):
    contagem = texto.lower().count('a')
    if contagem > 0:
        return f"A letra 'a' aparece {contagem} vezes na string."
    else:
        return "A letra 'a' não aparece na string."

# Teste com uma string específica
texto = input("Informe uma string: ")
print(contar_letra_a(texto))
