#valores alatorios
import random

lista = [1,2,3]
num = random.randint(0,10)#gerar numero aleatorio
num2 = random.choice(lista)
print(num)
print(num2)

#tratamento de exceções
a=int(input("a: "))#comando para imput
b=int(input("b: "))#comando para imput
try: #tente
	print(a/b)
except: #exceção
	print("Não existe divisão por 0")
