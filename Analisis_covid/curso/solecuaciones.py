import numpy as np
import sympy as sp
def biseccion(f, a, b, tol=1.0e-6):
    if a > b:
        return print("Intervalo mal definido")
    if f(a) * f(b) >= 0.0:
        return print("La función debe cambiar de signo en el intervalo")
    if tol <= 0:
        return print("La tolerancia de error debe ser un número positivo")
    else:
        x = (a + b) / 2.0
        while True:
            if b - a < tol:
                return x
            elif np.sign(f(a)) * np.sign(f(x)) > 0:
                a = x
            else:
                b = x
            x = (a + b) / 2.0


def SteffensenRoot(fun,xi,i,d):    # Se declara la funcion de nuestro codigo
    variable = "x"
    x = sp.Symbol(variable)
    y = sp.sympify(fun)
    print(y)    # Muestra al usuario la funcion sobre la que se trabaj
    
    
    p = 1/(10**d) 
    k = 0
    xi = float(xi)    # Se asegura que xi sea un valor numerico
    er = 1
    print("{:12}\t{:12}\t{:12}\t{:12}".format('i','hi','hr','er'))
    
    
    # Inicia el bubcle para iterar el metodo
    while k < i and er > p:
        # Evaluamos las ecuaciones por separadp
        # para mantener una mejor vista del codigo
        c = float(y.subs(x,xi).evalf()) 
        v = float(y.subs(x,xi+c).evalf())
        

        xr = xi -((c**2)/(v-c))    # Aplicamos el metodo Steffensen
        er = abs((xr-xi)/xr)    # Calculamos el error
        xi = xr    #Redefinimos el valor de xi
        k += 1
        leyenda = "{:}\t{:12}\t{:12}\t{:12}".format(k,round(xi,d),round(xr,d),round(er,d))
        print(leyenda)
        
        
    return print("La raíz a {:} dígitos de precisión es: {:}".format(d, round(xi,d)))

 
def newton(f, df, x_0, maxiter=50, xtol=1.0e-9, ftol=1.0e-9):
    x = float(x_0) 
    for i in range(maxiter):
        dx = -f(x) / df(x) 
        x = x + dx
        if abs(dx / x) < xtol and abs(f(x)) < ftol:
            return x
    raise RuntimeError("No hubo convergencia después de {} iteraciones").format(maxiter)