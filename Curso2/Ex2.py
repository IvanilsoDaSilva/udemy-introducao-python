# -*- coding: utf-8 -*-
nota=1.0
print("Programa que imforma se a nota esta aprovada ou reprovada")
while nota!=-1.0:
	print("A nota deve estar entre 0 e 10!")
	nota=float(input("Nota(-1 para sair): "))
	
	if nota>=6.0 and nota<=10.0:
		print("Aprovado\n")
	elif nota<6.0 and nota>=0.0:
		print("Reprovado\n")