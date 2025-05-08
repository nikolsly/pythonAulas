import os
os.system("cls")
os.system("color a")
#ESTRUTURAS CONDICIONAIS IF ELSE (ELIF)
#SWITCH CASE -> (matc case) escolha o caso(a partir da versão 3.10)
#match valor:
#  case valor:

# linguagem= 100

# match linguagem:
#     case ("python"):
#         print("é facil")
    
#     case "java":
#         print("muito codigo, python faz melhor com linhas menores")

#     case "c#":
#         print("massa")

#     case "js":
#         print("sou do back")

#     case "html":
#         print("Kauã não dorme")

#     case _ :
#         print("outro caso")

#print("1.Segunda 2.Terça 3.Quarta 4.Quinta 5.Sexta  6.Sábado 7.Domingo")

# semana= int(input("Digite a semana: "))

# match semana:
#     case 1:
#         print("Segunda")
#     case 2:
#         print("Terça")
#     case 3:
#         print('Quarta')
#     case 4:
#         print("Quinta")
#     case 5:
#         print("Sexta")
#     case 6:
#         print("Sábado")
#     case 7:
#         print("Domingo")


# print("*"*40, "MUNDO CELULAR", "*"*40)


# print("""
# 1- IPHONE 15 - R$:5000,00
# 2- XIAOMI REDMI 13 PRO PLUS 512GB - R$:2500,00
# 3- SAMSUNG S25 265 GB - R$:6999,00

# FRETE: SP -> 10,00
#        MG -> 15,00
#        RS -> 20,00
# """)

# celular= int(input("Digite o nº do produto: "))
# estado= (input("Digite a sigla do estado: "))

# match celular:
#    case "IPHONE 15":
#         preco= 5000 
#    case "XIOMI REDMI 13 PRO PLUS":
#         preco= 2500.00
#    case "SAMSUNG":
#         preco= 6999.00
#    case _:
#           preco= 0
#           print("Modelo invalido") 

# match estado:
#    case "SP":
#         frete= 10
#    case "MG":
#         frete= 15
#    case "RS":
#         frete= 20
#    case _:
#           frete= 0
#           print("Não foi possivel cacular")

#MATCH CASE IF

# valor = 0
# #rC
# valor = random.randint(0,100) #gera de 1 ate 99 aleatoriamente

# match valor:

#     case _ if valor <50 : 
#         print("menor que 50")
#     case _ if valor ==50:
#         print("= 50")
#     case _ if valor > 50:
#         print("maior que 50")
import random

print("*" * 20, "PEDRA, PAPEL E TESOURA", "*" * 20)

print("JOGO PEDRA PAPEL TESOURA ")

papel = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

pedra = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""


tesoura = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""

#pedra=1 papel=2 tesoura=3
mao = input("Digite pedra ou papel ou tesoura :")
maquina = random.randint(1,3)

match maquina :
    case 1:
        maquina = "pedra"
    case 2:
        maquina = "papel"
    case 3 :
        maquina ="tesoura"

match mao:

    case _ if mao== "pedra" and maquina=="pedra" :
        print(f"Maquina: {maquina} {pedra}")
        print(f"Você: {mao}  {pedra}")
        print("EMPATOU!")
    
    case _ if mao== "pedra" and maquina=="papel":
        print(f"Maquina: {maquina} {papel}")
        print(f"Você: {mao}  {pedra}")
        print("PERDEU!")
    case _ if mao== "pedra" and maquina=="tesoura":
        print(f"Maquina: {maquina} {tesoura}")
        print(f"Você: {mao}  {pedra}")
        print("GANHOU!")
    case _ if mao== "papel" and maquina=="papel":
        print(f"Maquina: {maquina} {papel}")
        print(f"Você: {mao}  {papel}")
        print("EMPATOU!")
    case _ if mao== "papel" and maquina=="pedra":
        print(f"Maquina: {maquina} {pedra}")
        print(f"Você: {mao}  {papel}")
        print("GANHOU")
    case _ if mao== "papel" and maquina=="tesoura":
        print(f"Maquina: {maquina} {tesoura}")
        print(f"Você: {mao}  {papel}")
        print("PERDEU!")
    case _ if mao== "tesoura" and maquina=="pedra":
        print(f"Maquina: {maquina} {pedra}")
        print(f"Você: {mao}  {tesoura}")
        print("PERDEU!")
    case _ if mao== "tesoura" and maquina=="papel":
        print(f"Maquina: {maquina} {papel}")
        print(f"Você: {mao}  {tesoura}")
        print("GANHOU!")
    case _ if mao== "tesoura" and maquina=="tesoura":
        print(f"Maquina: {maquina} {tesoura}")
        print(f"Você: {mao}  {tesoura}")
        print("EMPATOU!")
    case _:
        print("DIGITOU ERRADO! ESCOLHA PAPEL OU TESOURA OU PEDRA")
