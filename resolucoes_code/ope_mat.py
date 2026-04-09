# Vamos solicitar como entrada dois numeros e realizar uma operacao simples.

numero_1 = float(input("Digite o primeiro numero: "))
numero_2 = float(input("Digite o segundo numero: "))
operacao = input("Digite a operacao (+, -, *, /): ")

if operacao == "+":
	resultado = numero_1 + numero_2
elif operacao == "-":
	resultado = numero_1 - numero_2
elif operacao == "*":
	resultado = numero_1 * numero_2
elif operacao == "/":
	if numero_2 == 0:
		print("Erro: divisao por zero nao e permitida.")
	else:
		resultado = numero_1 / numero_2
		print("Resultado:", resultado)
else:
	print("Operacao invalida.")

if operacao in ["+", "-", "*"]:
	print("Resultado:", resultado)