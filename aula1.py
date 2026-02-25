import numpy as np

"""
#entradas, pesos, e bias
x = np.array([1, 0])
w = np.array([0.6, 0.4])
b = -0.5


#calculo de Z
z = np.dot(x,w) + b      #esse np.dot ele faz a multiplicação dos indices das array entao ta pegando o indice 0 de x e multiplicando pleo indice 0 de W
 
#função de ativação(step)
def step(z):
    return 1 if z > 0 else 0

#saida
y = step(z)

#estrutura de saida
print("Z =", z)
print("Saida = ", y)
"""



#-------------------------------
# exercicio 
#1. dados os valores de entrada, peso e bias. calcule o valor de Z, use a função degrau e deterine o valor de saida. R: valor de saida z= 0.95 | y = 1
# x1= 0.8| x2= 0.5 | w1 = 0.7 | w2 = -0.6 | b = 0.1

#entradas, pesos, e bias
x = np.array([0.8, 0.5])
w = np.array([0.7, -0.6])
b = 0.1


#calculo de Z
z = np.dot(x,w) + b      
 
#função de ativação(step)
def step(z):
    return 1 if z > 0 else 0

#saida
y = step(z)

#estrutura de saida
print("Z =", z)
print("Saida = ", y)




#caso o valor de w1 mude para -1.4, o que acontece com a saida? R: ele fica negativado com o valor de z de -0.719 fazendo com que o neuronio n ative
x = np.array([0.8, 0.5])
w = np.array([-1.4, -0.6])
b = 0.1


#calculo de Z
z = np.dot(x,w) + b      
 
#função de ativação(step)
def step(z):
    return 1 if z > 0 else 0

#saida
y = step(z)

#estrutura de saida
print("Z =", z)
print("Saida = ", y)

#qual a função ou objetivo do peso na decisão R: 


