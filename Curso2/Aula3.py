# -*- coding: utf-8 -*-
#variáveis
string1="Ola"
string2="Mundo"
string3="!"

#string1 - operações
concatenar = string1+" "+string2+string3 # concatenar string
print(concatenar)
print(len(concatenar))#tamanho da string
print(concatenar[0]+concatenar[1]+concatenar[2])#valor na posicao da string
print(concatenar[0:4]+concatenar[4:])#valor de uma parte da string

#string2 - metodos
print("\n"+concatenar.lower())#minusculo
print(concatenar.upper())#maiusculo 
print(concatenar.strip())#remove espaços e caracter especiais
print(concatenar.split(" "))#converte o string em lista'
print(concatenar.find("Mundo!"))#posição da palavra/letra
print(concatenar.replace("Ola", "Olá"))#substitui string