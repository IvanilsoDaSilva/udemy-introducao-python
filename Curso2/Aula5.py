# -*- coding: utf-8 -*-
#lista1
lista1 = ["Iva", "Vini", "Tiao", "Celo"]
lista2 = [1,2,3,4,5]
lista3 = ["Ivanilso", 18,1.7, True]

print(lista1)
print(lista2)
print(lista3)
print("")

print(lista1[2])#item na posição
print("")

for item in lista1: #for retornando todos itens da lista 
	print(item)
print("")

print(len(lista1))#tamanho da lista
print("")

lista1.append("Dani")#adiciona ao final da lista
print(lista1)
print("")

print("Iva" in lista1)#se item pertence a lista
print("")

del lista2[3:]#apagar da lista
print(lista2)
lista4=[]#cria lista em branco
print("########################################################################")

#lista2
lis1 = [3,1,7,5,9,2,4,8,6]
print(sorted(lis1)) #retorna a lista ordenada mais não altera a lista
lis1.sort(reverse=True) #ordena o valor da lista(decrescente)
print(lis1)
lis1.reverse() #inverte a lista
print(lis1)
#funciona com letras(alfabeto)