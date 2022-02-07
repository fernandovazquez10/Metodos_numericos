def trapecio(x, y):
    # Cantidad de datos
    n = len(x)
    
    # Intervalo de integración
    a = x[0]
    b = x[n-1]

    suma = sum([tmp for tmp in y[1:n-1]])
    I = (b - a) * (y[0] + y[n-1] + 2*suma) / (2*(n-1))
    
    return I