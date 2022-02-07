# Utilizaremos la libreria sympy para
# graficar la ecuacion y volver simbolos la variable y ecuacion
import sympy as sp 

def SteffensenRoot(fun,xi,i,d):    # Se declara la funcion de nuestro codigo
    variable = "x"
    x = sp.Symbol(variable)
    y = sp.sympify(fun)
    print(y)    # Muestra al usuario la funcion sobre la que se trabaja
    
    
    p = 1/(10**d) 
    k = 0
    xi = float(xi)    # Se asegura que xi sea un valor numerico
    er = 1
    print("{:12}\t{:12}\t{:12}\t{:12}".format('i','xi','xr','er'))
    
    
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
    
