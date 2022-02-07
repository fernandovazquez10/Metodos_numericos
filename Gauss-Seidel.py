
"""
Problema 1
resolver matriz
"""
import numpy as np

#Ingresando la matriz
A = np.array([[1,4,9],
              [4,9,16],
              [9,16,25]])
#Ingresando el vector
B = np.array([[14],
              [29],
              [50]])

#Matriz aumentada
AB = np.concatenate((A,B),axis=1)
AB0 = np.copy(AB)

#pivoteo por filas

tam = np.shape(AB)
n = tam[0]
m = tam[1]

for i in range(0,n-1,1): 
    col = abs(AB[i:,i])
    dondemax = np.argmax(col)
    
    #Intercambio de filas
    if dondemax !=0:
        temp = np.copy(AB[i,: ])
        AB[i,:] = AB[dondemax + i,:]
        AB[dondemax + i,:] = temp

#SAlida
print("Matriz aumentada")
print(AB0)
print("Pivoteo por filas Matriz")
print(AB)

#Recuperar matriz y vector
a = AB[0, 0:3].tolist()
b = AB[1, 0:3].tolist()
c = AB[2, 0:3].tolist()

A1 = np.array([a,b,c])
B1 = np.transpose([AB[0: , -1]])

#Iniciando el metodo de Gauss-Seidel

X0 = np.array([0.0,0,0])

tolera = 0.00001
kmax = 100

size = np.shape(A1)
n1 = size[0]
m1 = size[1]

X = np.copy(X0)
dif = np.ones(n1, dtype=float)
error = tolera*2 

k=0
while error> tolera and k < kmax:
    for j in range(0,n1,1):
        suma = 0
        for q in range(0,m1,1):
            if j != q:
                suma = suma-A1[j,q]*X[q]
        
        nuevo = (B1[j]+suma)/A1[j,j]
        dif[j] = np.abs(nuevo-X[j])
    error = np.max(dif)
    k += 1 
    
X=np.transpose([X])

if k == kmax:
    print("El sistema no converge")
print("respuesta X: ")
print(X)

    
    
    




