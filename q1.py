#1) Pedir os números pro usuário
lista_num = []
while True:
    valor = int(input("Digite números meu chegado: "))
    if valor < 0:
        break
    else:
        lista_num.append(valor)
#2) Declarar intervalos
intervalo_1 = 0
intervalo_2 = 0
intervalo_3 = 0
intervalo_4 = 0
#3) Ler os dados e colocar nos intervalos
for num in lista_num:
    if num > 0 and num <= 25:
        intervalo_1 += 1
    elif num >= 26 and num <= 50: 
        intervalo_2 += 1
    elif num >= 51 and num <= 75:
        intervalo_3 += 1
    elif num >= 76 and num <= 100:
        intervalo_4 += 1
#4) Printar os resultados
print("Quantidade de números entre 1 e 25: ", intervalo_1)
print("Quantidade de números entre 26 e 50: ", intervalo_2)
print("Quantidade de números entre 51 e 75: ", intervalo_3)
print("Quantidade de números entre 76 e 100: ", intervalo_4)
