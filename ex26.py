# execrcicio 26 Menu simples de pedido

print("1 - Hambúrguer - R$ 15.00")
print("2 - Pizza - R$ 20.00")
print("3 - Refrigerante - R$ 8.00")

opcao = int(input("Escolha uma opcao: "))

if opcao == 1:
    print("Você escolheu Hambúrguer")
    print("Valor: R$ 15.00")
elif opcao == 2:
    print("Você escolhe uma pizza")
    print("Valor: R$ 20.00")
elif opcao == 3:
    print("Você escolheu Refrigerante")
    print("Valor: R$ 8.00")
else:
    print("Opção inválida")