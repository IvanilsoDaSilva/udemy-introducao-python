# -*- coding: utf-8 -*-
idade=1
print("Programa para indentificar maior e menor idade")
while idade!=0:
	print("A idade deve ser positiva")
	idade=int(input("Idade(digite 0 para sair): "))
	if idade<18 and idade>0:
		print("Menor de idade\n")
	elif idade>=18:
		print("Maior de idade\n")