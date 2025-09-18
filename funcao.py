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

# # q7:
# def fatorial(n):
#     fat = 1
#     for n in range(n, 1,-1):
#         fat = fat * n
#     print(f"O fatorial do número digitado é: {fat}.")

# fatorial(10)

# q8:
# def palavra(palavra):
#     palavra_str = str(palavra)
#     vogais = "aAáÁàÀâÂãÃeEéÉêÊiIíÍoOóÓôÔõÕuUúÚ"
#     contador = 0
#     for caractere in palavra_str:
#         if caractere in vogais:
#             contador += 1
#     print(f"A palavra {palavra} tem {contador} vogais.")
# palavra("Guilherme")

# # q9:
# from random import randint 
# numero = randint(1, 20)
# while True:
#     n = int(input("Digite um número: "))
#     if n > numero:
#         print("O número que você digitou é maior")
#         n = int(input("Tente novamente: "))
#     elif n < numero:
#         print("O número que você digitou é menor")
#         n = int(input("Tente novamente: "))
#     elif n == numero:
#         print("Você acertou!")
#         break

# # q10
# n = int(input("Digite um número: "))
# par = 0
# for i in range(n):
#     if i % 2 == 0:
#         par += i
# print(f"A soma dos pares é: {par}") 

# # q11
# def calculadora():
#     print("1 - soma, 2 - subtração, 3 - Multiplicação, 4 - Divisão")
#     n1 = float(input("Digite um número: "))
#     n2 = float(input("Digite um número: "))
#     operacao = int(input("Digite a operação: "))
#     if operacao == 1:
#         print(f"{n1 + n2}")
#     if operacao == 2:
#         print(f"{n1 - n2}")
#     if operacao == 3:
#         print(f"{n1 * n2}")
#     if operacao == 4:
#         print(f"{n1 / n2}")

# calculadora()

#q12
def primo(n):
    raiz = n**0.5
    for i in range(raiz):
        if n / i == 0:
           e_primo = False
        if n / i != 0:
           e_primo = True
           return e_primo
        e_primo = print("é primo")
primo(7)