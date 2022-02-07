"""
Resolver matriz importada de un CVS
usando el metodo de Gauss-Jordan
"""
import numpy as np 


data = np.genfromtxt("matriz.csv",delimiter=",")

AB = np.delete(data,(0),axis=0)

AB0 = np.copy(AB)

tam = np.shape(AB)
n = tam[0]
m = tam[1]

for i in range(0,n-1,1):
    col = abs(AB[i:,i])
    dondemax = np.argmax(col)
    
    if (dondemax !=0):
        temp = np.copy(AB[i,:])
        AB[i,:] = AB[dondemax+i,:]
        AB[dondemax+i,:] = temp
        
AB1 = np.copy(AB)

for i in range(0,n-1,1):
    pivote = AB[i,i]
    adelante = i + 1
    for k in range(adelante,n,1):
        factor = AB[k,i]/pivote
        AB[k,:] = AB[k,:] - AB[i,:]*factor
AB2 = np.copy(AB)


ultfil = n-1
ultcol = m-1
for i in range(ultfil,0-1,-1):
    pivote = AB[i,i]
    atras = i-1 
    for k in range(atras,0-1,-1):
        factor = AB[k,i]/pivote
        AB[k,:] = AB[k,:] - AB[i,:]*factor

    AB[i,:] = AB[i,:]/AB[i,i]
X = np.copy(AB[:,ultcol])
X = np.transpose([X])


print("Matriz aumentada:")
print(AB0)
print("Pivoteo parcial por filas")
print(AB1)
print("eliminacion hacia adelante")
print(AB2)
print("eliminación hacia atrás")
print(AB)
print("solución de C: ")
print(X)