# -*- coding: utf-8 -*-
dic = {"Iva":1, "Vini":2, "Tiao":3}

print(dic["Iva"])#selecionando valor da chave Iva
print(dic)
print(" ")

for chave in dic:
	print(chave,":",dic[chave])
print(" ")

for i in dic.items():
	print(i)
print("")

for x in dic.values():
	print(x)