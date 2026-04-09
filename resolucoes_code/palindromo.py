# Verifique se uma palavra e um palindromo.

palavra = input("Digite uma palavra: ").strip().lower()

if palavra == palavra[::-1]:
    print("E um palindromo.")
else:
    print("Nao e um palindromo.")
