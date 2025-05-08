import os
os.system("cls")
os.system("color a")

#Continuação Input com Int e Float
#int() -> converte para inteiro
#float -> converte para numero quebrado

# numero = 10
# numero2 = input("digite um numero:")
# print("o tipo de numero é,", type(numero2))
# soma = numero + int(numero2)
# print(f"soma de {numero} + {numero2}=", soma)

#exemplo2
# num1= input("digite um umero:")
# soma = float(num1) + 15
# print("A soma de",num1, "+" "15" , "=", soma )

#exemplo 3
# n1 = int(input("Digite um numero:"))
# n2 =  int(input("digite outro numero:"))
# soma = (n1)+(n2)
# print(f"a soma de {n1} + {n2}=", soma)

# #Atividade 1
# n1 = int(input("Digite um numero:"))
# n2 =  int(input("digite outro numero:"))
# multiplicação = (n1)*(n2)
# print(f"a soma de {n1} * {n2}=", multiplicação)

# #Atividade 2
# numero = int(input("Digite um número: "))
# antecessor = numero - 1
# sucessor = numero + 1
# print(f"Antecessor: {numero}  {antecessor} ")
# print(f"Sucessor: {numero} {sucessor}")

# #Atividade 3
# ano_atual = 2025
# ano_nascimento = int(input("Digite o seu ano de nascimento: "))
# idade = ano_atual - ano_nascimento
# print(f"Você tem {idade} anos.")

#Escreva  um programa em python que leia 2 itens de um supermercado
#voce deve armazenar o nome do valor do item, no final aplique 10% de desconto
#no primeiro item, 25% de desconto no segundo item.
#Calcule o valor total da compra e mostre o nome  eo valor  com desconto de cada item
            
            #Atividade 1
print("="*20, "SUPERMERCADO", "="*20)
nome1=input("Digite o nome do produto:")
valor1=float (input("Digite o valor do produto:"))

nome2=input("Digite o nome do produto:")
valor2=float (input("Digite o valor do produto:"))

desconto1=0.10*valor1
desconto2=0.25*valor2
valor_final1 = round(valor1-desconto1)
valor_final2 = round(valor2-desconto2)

print("="*20, "CAIXA", "="*20 )

print(f"O {nome1} custa {valor1} e com 10% de desconto é {valor_final1}")
print(f"O {nome2} custa {valor2} e com 25% de desconto é {valor_final2}" )


print("="*20, "TOTAL", "="*20 )

total = valor_final1+valor_final2
print(f"TOTAL DA COMPRA -> R$:{total}")



