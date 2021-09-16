bebidas = input("Qual bebida vc quer? A - Agua \nB -  Coca Cola  \nC - Vinho ").lower()

if bebidas == "a":
    print("Você escolheu água, que custa 2R$")
elif bebidas == "b":
    print("Você escolheu Coca Cola, que custa 5R$")
elif bebidas == "c":
    print("Voce escolheu vinho, que custa 6R$")

else:
    print("Valor Inexistente")    