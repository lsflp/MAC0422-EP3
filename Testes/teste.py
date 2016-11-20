from gerenciador import *
import time
teste = "teste.txt"
num = 30

tempos1 = [] 
tempos2 = []
tempos3 = []
tempos4 = []

for i in range(0, num):
	print ("First Fit")
	start = time.time()
	read_file(teste)
	espaco(1)
	substitui(1)
	executa(1)
	end = time.time()
	tempos1.append(end-start)

for i in range(0, num):
	print ("Next Fit")
	start = time.time()
	read_file(teste)
	espaco(2)
	substitui(1)
	executa(1)
	end = time.time()
	tempos2.append(end-start)

for i in range(0, num):
	print ("Best Fit")
	start = time.time()
	read_file(teste)
	espaco(3)
	substitui(1)
	executa(1)
	end = time.time()
	tempos3.append(end-start)

for i in range(0, num):
	print ("Worst Fit")
	start = time.time()
	read_file(teste)
	espaco(4)
	substitui(1)
	executa(1)
	end = time.time()
	tempos4.append(end-start)

print (tempos1)
print (tempos2)
print (tempos3)
print (tempos4)