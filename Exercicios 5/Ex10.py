#10.Uma loja tem uma política de descontos de acordo com o valor da compra do cliente.
# Os descontos começam acima dos R$500.
# A cada 100 reais acima dos R$500,00 o cliente ganha 1% de desconto cumulativo até 25%.
# Por exemplo:R$500=1%||R$600,00=2%,etc.
# Faça um programa que exiba essa tabela de descontos no seguinte formato:
# Valor da Compra – Porcentagem de Desconto – Valor Final
print("Valor da Compra - Porcentagem de Desconto - Valor Final")
desc = 1
valorCompra = 100
for i in range(1,30):
    valorCompra = 100*i
    if i<5:
        print(valorCompra,"- 0% -", valorCompra)
    elif i>4 and i<=30:
        desc = (i-4)
        print(valorCompra,"-",str(desc)+"%","-",valorCompra-(valorCompra*(desc/100)))