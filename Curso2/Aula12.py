#zip

lista1 = [1,2,3,4,5]
lista2 = ["abacate", "bola", "cachorro", "dinheiro", "elefante"]
lista3 = ["RS 2,00", "RS 5,00", "null", "null", "null"]

for numero, nome, valor in zip(lista1, lista2, lista3):
	print(numero, nome, valor)