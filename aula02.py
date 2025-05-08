import os
os.system("cls")
os.system("color a")
#Aula02 -> variaveis, tipos e input
#Tipos de dados
#String -> Texto
#Int -> Inteiro
#Float -> Quebrado (flutuante)
#Declaração de variaveis
# escola = "senai"
# #mostrando o valor da variaveis no print
# #conectando com o +
# print("o nome da minha escola:" + escola)
# #separando por parametro
# print(f"o nome da minha escola é {escola}")

# #exemplo de variavel int
# numero=100
# print("somando com 10 =",numero+10)
# print("subtarindo 5 =",numero -5)
# print("dividindo por 2 = ",numero/2)
# print("multiplicando por 10 =", numero*10)
# nome="Nicolas Levy Guimarães Marinho"
# print("o meu nome é", nome)
# cpf="423.172.168-82"
# print("o meu CPF é", cpf)
# idade="16 anos"
# print("eu tenho", idade)

# #input
# #obrigatoriamente  antes do input deve existir uma variavel
# #resumindo
# #input() -> pergunta algo a ser armazenado
# #print() -> mostra texto na tela
# texto= input("digite algo:")
# print("voce digitou ... ", texto)
print("*"*10, "CADASTRO","*"*10)
nome = input("Digite seu nome:")

CPF= input("Digite seu CPF:")

RG= input("Digite seu RG:")

print("*"*10, "DADOS CADASTRADOS", "*"*10)
print("nome:", nome)
print("CPF:", CPF)
print("RG:", RG)