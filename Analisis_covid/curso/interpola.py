import numpy as np 

def newton(X,Y,x):
    """
         Calcular la interpolación en x puntos
    """
    sum=Y[0]
    temp=np.zeros((len(X),len(X)))
         # Asignar la primera línea
    for i in range(0,len(X)):
        temp[i,0]=Y[i]
    temp_sum=1.0
    for i in range(1,len(X)):
                 #x polinomio
        temp_sum=temp_sum*(x-X[i-1])
                 # Calcular diferencia de medias
        for j in range(i,len(X)):
            temp[j,i]=(temp[j,i-1]-temp[j-1,i-1])/(X[j]-X[j-i])
        sum+=temp_sum*temp[i,i] 
    return sum