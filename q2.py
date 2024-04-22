#1) Mostrar cardapio
print("CARDÁPIO")
print("Especificação\tCódigo\tPreço\nCachorro Quente\t101\tR$1,20\nBauru Simples\t102\tR$1,30\nBauru com ovo\t103\tR$1,50\nHamburguer\t104\tR$1,20\nCheseburguer\t105\tR$1,30\nRefrigerante\t106\tR$1,00")

#2) Declarar listas e o dicionario de preco por codigo
precos = {101: 1.20, 102: 1.30, 103: 1.50, 104: 1.20, 105: 1.30, 106: 1.00}
lista_pedidos = []
lista_qtd = []

#3) Receber o pedido do cliente
while True:
    cod_pedidos = int(input("Digite o código do produto que deseja: "))
    lista_pedidos.append(cod_pedidos)
    qtd_pedido = int(input("Digite a quantidade do produto que deseja: "))
    lista_qtd.append(qtd_pedido)
    resp = input("Deseja algo mais ? [sim, não] \n")
    if resp == "sim":
        continue
    else:
        break
#4) Declarar a variavel de total
total_pedido = 0
#5)  Calcular o total do pedido usando o dicionario de precos por codigo e printar o total em uma tabela
print("\nRESUMO DO PEDIDO:")
for i in range(len(lista_pedidos)):
    codigo = lista_pedidos[i]
    qtd = lista_qtd[i]
    preco_unitario = precos.get(codigo, 0)
    total_item = qtd * preco_unitario
    total_pedido += total_item
    print(f"{codigo}\t{precos[codigo]}\t{qtd}\t{preco_unitario}\t{total_item}")

print("\nTotal a pagar:", total_pedido)
