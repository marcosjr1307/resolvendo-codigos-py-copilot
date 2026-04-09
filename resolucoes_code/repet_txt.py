# Vamos solicitar uma string e um numero inteiro como entrada.
# Depois retornamos a string repetida a quantidade informada.

texto = input("Digite um texto: ")
quantidade = int(input("Digite a quantidade de repeticoes: "))

resultado = texto * quantidade
print("Texto repetido:", resultado)