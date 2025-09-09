# # q1:
# def saudacao(nome):
#     print(f'Olá, {nome}! Seja bem-vindo ao curso de lógica de programação.')
# saudacao("guilherme")

# # q2:
# def par_impar(n):
#     if n % 2 == 0:
#         print(f"{n} é par")
#     else:
#         print(f"{n} é ímpar")
# par_impar(7)

# # q3:
# def maior(n1,n2):
#     if n1 == n2:
#         print("São iguais")
#     if n1 > n2:
#         print(f"{n1} é maior que {n2}")
#     if n2 > n1:
#         print(f"{n2} é maior que {n1}")
# maior(1789,1969)
    
# # q4:
# def tabuada(n):
#     for i in range(1, 11):
#         print(n * i)
# tabuada(7)

# # q5:
# for i in range(10, -1, 0 - 1):
#     print(i)
# print("Papoco")

# q6:
# contador = 0
# n = int(input("Digite a quantidade de nota: "))
# for i in range(n):
#     notas = int(input("Digite a nota: "))
#     contador = contador + notas
# media = contador / n
# print(media)

# q7:
n=int(input("Digite um número qualquer para calcular seu fatorial: "))
fat = 1
for n in range(n,1,-1):
    fat=fat*n
print(f"O fatorial do número digitado é: {fat}.")

# q8:
palavra=input("Digite uma palavra qualquer: ")
vogais="aAáÁàÀâÂãÃeEéÉêÊiIíÍoOóÓôÔõÕuUúÚ"
contador=0
for caractere in palavra:
    if caractere in vogais:
        contador+=1
print(f"A palavra {palavra} tem {contador} vogais.")

# q9:
n = int(input("Digite um número:"))