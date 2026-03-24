# exercicio 25 - Desconto do pedido

produto =input("digite o nome produto:")
preço = float(input("digite o preço d produto:R$"))
quantidade =int(input("digite a quantidade"))

total=preço * quantidade

if total>50:
    desconto =total * 0,10
    total_final=total-desconto
    print("desconto aplicado:10%")
else:
    total_final=total
    print("sem desconto")

    print(f"produto:{produto}")
    print(f"total a pagar:R$ {total_final:.2f}")
