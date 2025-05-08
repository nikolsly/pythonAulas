#ESTRUTURA CONDICIONAL IF ELSE (se senao) -> True or False (Verdadeiro ou Falso)
#OPERADORES CONDICIONAIS:  > >= < <= != == and or
# > (maior)
# >= ( maior OU igual)
# < (menor)
# <= (menor OU igual)
# == (igual) 
# != (diferente)
# and (e) -> Se apenas uma ou mais condiçoes for FALSA ele retorna FALSE 
# or (ou) -> Se apenas uma ou mais condições for VERDADE ele retorna TRUE

#if condicao :
# print("verdade")
#else: 
#print("falso")

# A IDENTAÇÃO (ESPAÇO) deve ser utilizado o TAB


# x=10  
# if x > 1000:
#     print("verdade")
# else:
#     print("falso")
#     print("falso")
#     print("falso")
#     print("falso")

# nome = "teste"
# if "testee" != nome:
#     print(1)
# else:
#     print(2)

import os
os.system("cls")
os.system("color a")

             #Atividade 1
# idade = int(input("Digite sua idade: "))

# if idade >= 18:
#      print("Você é maior de idade.")
# else:
#      print("Você é menor de idade.")

# idade= int(input("Digite sua idade:"))
# if idade == 0 or idade >120:
#     print("Idade invalida")
# else :
#     print("Valida")

# email= (input("Digite seu e-mail:"))
# senha= (input("Digite sua senha:"))

# if "python@senai.com"== email:
#     if "12345678" == senha:
#         print("Usuario autenticado")
# else:
#     print("Senha ou usuario invalido")           



#As maçãs custam R$ 0,30 cada se forem compradas menos do que 
#uma dúzia, e R$ 0,25 se forem compradas pelo menos doze. 
#Escreva um programa que leia o número de maçãs compradas, 
#calcule e escreva o valor total da compra


print("="*20, "DANIEL'S HORT FRUIT", "="*20)

numero_macas = int(input("Digite o número de maçãs compradas: "))

if numero_macas < 12:
    preco_por_maca = 0.25
else:
    preco_por_maca = 0.30

valor_total = numero_macas * preco_por_maca

print(f"O valor total da compra é R$ {valor_total:.2f}")

