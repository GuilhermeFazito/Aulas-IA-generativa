import numpy as np

# o @ ele multiplica os valores ao longo da matriz



#variaveis de entrada
x= np.array ([1,2])

#pesos e bias 
w1 = np.array([[0.5, -0.4],
               [0.3, 0.8],
               [-0.6, -0.2]])

b1 = np.array([0.1, 0.2, 0.05])

#função de ativação
def relu(z):
    return np.maximum(0,z)

#calculo da camada oculta (z= w*x + b)
z1 = w1 @ x + b1 
a1 = relu(z1)

#pesos e bias da camada de saida
w2= np.array([0.7, 0.5, 0.9])
b2 = 0.2

#saida
z2= w2 @ a1 + b2



#função de ativação para classificação
def sigmoide(z):
    return 1/ (1+np.exp(-z))

#saida final
y_regressao= z2
y_classificacao = sigmoide(z2)


#exibe os resultados
print (y_classificacao)
print(y_regressao)