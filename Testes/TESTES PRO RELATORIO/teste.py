from gerenciador import *
#import time
teste = "../trace2.txt"
num = 1

for i in range(0, num):
	print ("First Fit")
	read_file(teste)
	espaco(1)
	substitui(1)
	executa(20)

for i in range(0, num):
	print ("Next Fit")
	read_file(teste)
	espaco(1)
	substitui(2)
	executa(20)

for i in range(0, num):
	print ("Best Fit")
	read_file(teste)
	espaco(1)
	substitui(3)
	executa(20)

for i in range(0, num):
	print ("Worst Fit")
	read_file(teste)
	espaco(1)
	substitui(4)
	executa(20)


#start = time.time()
#print("hello")
#end = time.time()
#print(end - start)
