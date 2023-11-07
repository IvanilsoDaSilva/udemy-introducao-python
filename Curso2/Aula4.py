# -*- coding: utf-8 -*-
#funçães
def soma(x, y):
	return x+y
def multiplicacao(x,y):
	return x*y

print(soma(2,3))
print(multiplicacao(2,3))

#arquivos 
print(" ")
arquivoR = open("Aula4/arquivo.txt")
arquivoW = open("Aula4/arquivo2.txt", "w")#w subescrever,a escrever

#textlinhas = arquivo.readlines() #ler linhas 
#print(textlinhas) 

text = arquivoR.read() #ler arquivo
print(text)

arquivoW.write("Esse é meu arquivo\n")
arquivoW.close()
