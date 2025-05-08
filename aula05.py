#import os
#os.sytem("cls")
#IF ENCADEADO -> testa todas as condiçoes mesmo se for uma verdadeira
#ELIF -> testa todas as condiçoes ate uma ser verdadeira

# x = 15

# if x <= 20 :
#     print("entrou no if 14")
# if x <=15 :
#     print("entrou no if 15")
# if x <=16:
#     print("entrou no if 16")


# if x <=20:
#     print("entrou no if 14")
# elif x<=15:
#     print("entrou no if 15")
# elif x <=16:
#     print("entrou no if 16")


# ESCREVA UM PROGRAMA EM PYTHON NA QUAL O USUARIO DIGITA A IDADE
#  SE MENOR QUE 12 -> CRIANÇA
#  SE MENOR QUE 18 -> ADOLESCENTE
#  SE MENOR QUE 60 -> ADULTO
#  SE NAO -> IDOSO


# NO CASO SE USAR IF ELE VAI TESTAR TODAS AS CONDIÇÕES
# idade = int(input("digite sua idade: "))

# if idade < 12:
#     print("criança")
# if idade < 18:
#     print("adolescente")
# if idade < 60:
#     print("adulto")
# else: 
#     print("IDOSO")


# # SE USAR ELIF ELE VAI TESTAR UMA E SAIR DA ESTRUTURA
# if idade < 12:
#     print("criança")
# elif idade < 18:
#     print("adolescente")
# elif idade < 60:
#     print("adulto")
# else: 
#     print("idoso")

#ativ.1
#replace("valor1","valor2") -> substitui o valor 1 pelo 2

#notas

# nota1 = float(input("digite sua 1º nota: ").replace(",","."))
# nota2 = float(input("digite sua 2º nota: ").replace(",","."))

# media = (nota1+nota1)/2
# #:.f -> formata para 2 casas decimais apenas no fstring(f)
# print(f"MÉDIA: {media:.2f}")

# if media  <5:
#     print("REPROVADO!")
# elif media >=5 and media<=7:
#     print("EM RECUPERAÇAO!")
# else:
#     print("APROVADO!")

#atividade sobre peso

# print("**********IMC**********")
# altura = float(input("diga sua altura: ").replace(",","."))
# peso = float(input("diga seu peso: ").replace(",","."))
# imc = peso /(altura * altura)

# print(f"seu imc é: {imc:.2f}")

# if imc <=17 :
#     print("MUITO ABAIXO DO PESO!")
# elif imc >17 and imc <=18.49 :
#     print("ABAIXO DO PESO!")
# elif imc >18.50 and imc <=24.99 :
#     print("PESO NORMAL!")
# elif imc >25 and imc <=29.99 :
#     print("ACIMA DO PESO!")
# elif imc >30 and imc <=34.99 :
#     print("OBESIDADE I!")
# elif imc >35 and imc <=39.99 :
#     print("OBESIDADE II!")
# else :
#     print("OBESIDADE III(mórbida)")

# raw string 
print("=====================REAJUSTE AUTOCAR=====================")


print (r"""                     
                                               
        _______      
       //  ||\ \     
 _____//___||_\ \___ 
 )  _          _    \
 |_/ \________/ \___|
___\_/________\_/____                         
                                                  """)
print("==========================================================") 
print("TABELA DE AJUSTES DE SALARIO: ")
print("Salarios de até R$ 2799,99 :aumento de 20%; ")
print("Salários entre R$ 2800,00 e R$6999,99: aumento de 15%;")
print("Salários entre R$ 7000,00 e R$ 14999,99: aumento de 10%;")
print("Salários de R$ 15000,00 em diante: aumento de 5%")
print("----------------------------------------------------------")
salario = float(input("digite seu salario: "))
percentual = 0
if salario <= 2799.99 :
    percentual= 0.20
elif salario >= 2800 and salario <= 6999.99 :
    percentual= 0.15
elif salario >= 7000 and salario <= 14999.99 :
    percentual= 0.10
else:
    percentual=0.05
print("------------------------REAJUSTES-------------------------") 
print(f"salario anterior ao reajuste R$: {salario}")
print(f"porcentual aplicado: {percentual*100} %")
print(f"valor do aumento: {salario * percentual}")
print(f"novo salario R$: {salario + (salario * percentual)}")




   