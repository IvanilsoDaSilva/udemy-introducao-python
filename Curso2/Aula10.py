#map

def dobro(x):
	return x*2

valor = [1,2,3,4,5]

valorDobrado = map(dobro, valor)

for v in valorDobrado:
	print(v)

print(" ")
valorDobrado = list(valorDobrado)
print(valorDobrado)