n1 = int(input("Digite um numero "))
n2 = int(input("Digite outro numero "))
operacao = input("Adição - + Subtraçao - -")

if operacao == "+":
    print(n1+n2)
elif operacao == "-":
    print(n1-n2)
else:
    print("valor invalido")        