from math import sqrt
import math

a=0.0
b=0.0
c=0.0
x=0.0
x1=0
x2=0
delta = 0.0
continuar = True
resposta = "null"


print("\n------- Programa que informa os valores de x em uma equação de segundo grau -------")
while(continuar==True):
	print("\n---------------------------------------------------------------------------")
	print("f(x)=( a * ( x )^2) + ( b * x ) + c")
	print("a deve ser diferente de 0\n")

	a=float(input("a: "))
	while a==0.0:
		a=float(input("a: "))
	print("f(x)=(",a," * ( x )^2) + ( b * x ) + c\n")
	b=float(input("b: "))
	print("f(x)=(",a," * ( x )^2 ) + (",b,"* x ) + c\n")
	c=float(input("c: "))
	print("f(x)=(",a," * ( x )^2 ) + (",b,"* x ) +",c,"\n")
	x=float(input("x: "))
	print("f(x)=(",a," * (",x,")^2) + (",b,"*",x,") +",c,"\n")
	
	delta = (b*b) - (4*a*c)
	if delta>=0: 
		x1 = (((-b) + math.sqrt(delta)) / (2*a))
		x2 = (((-b) - math.sqrt(delta)) / (2*a))

	if(delta<0):
		print("Delta: ", delta)
		print("Raiz nâo pertence aos numeros reais")
	if(delta==0):
		print("Delta: ", delta)
		print("raiz unica, x=",x1)
	if(delta>0):
		print("Delta: ", delta)
		print("x' =",x1,"\n")
		print("x'' =",x2)

	while resposta!="sim" and resposta!="nao" :
		resposta=str(input("\nContinuar? 'sim' ou 'nao': "))
	a=0.0
	b=0.0
	c=0.0
	x=0.0
	x1=0.0
	x2=0.0
	delta=0.0
	
	if resposta=="sim":
		resposta="null"
		contuinuar=True
		continue
	else:
		resposta="null"
		continuar=False
		continue


print("Fim")
