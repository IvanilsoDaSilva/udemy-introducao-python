x=0.0
y=0.0
sinal="vazio"
continuar=True
resposta="null"

while continuar==True:
	print("\n -------- calculadora -------- \n")
	sinal=str(input("Operação(+, -, *, /): "))
	while sinal!="+" and sinal!="-" and sinal!="*" and sinal!="/":
		sinal=str(input("Operação(+, -, *, /): "))
	print("\n",x,sinal,y)
	x=float(input("X: "))
	print(x,sinal,y)
	y=float(input("Y: "))

	if sinal=="+":
		print(x,sinal,y,"=",x+y)
	if sinal=="-":
		print(x,sinal,y,"=",x-y)
	if sinal=="*":
		print(x,sinal,y,"=",x*y)
	if sinal=="/":
		print(x,sinal,y,"=",x/y)

	while resposta!="sim" and resposta!="nao" :
		resposta=str(input("\nContinuar? 'sim' ou 'nao': "))
	x=0.0
	y=0.0
	sinal="vazio"
	if resposta=="sim":
		resposta="null"
		contuinuar=True
		continue
	else:
		resposta="null"
		continuar=False
		continue