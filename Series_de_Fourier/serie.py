# Importar módulo para el uso de matemáticas simbólicas
import sympy as sp
from sympy.abc import n
import matplotlib.pyplot as mp
# Se declaran como simbolos las variables 
# convirtiendo un str en un simbolo
x = sp.Symbol('x')
pi = sp.Symbol('pi')
# Ahora si, se ingresa la ecuación en formato str
equa = input('Ingresar la ecuación a expandir: ')

# Se "sympyfica" la cadena de texto ingresada, esto es que pasa a ser una
# variable del tipo "SYMPY"
y = sp.sympify(equa)

# Ingresamos el periodo
per = input('Ingrese el periodo: ')
# Convertimos el periodo en sympyfico
k = sp.sympify(per)
# Definimos el valor de Pi
w = sp.pi
# Sustituimos el valor de pi en caso de estar presente
per  = k.subs(pi,w)

# Procedemos a determinar el intervalo
l = per/2
limi = -l 
lims = l
print("")
print('-'*50)

# Se calculan los coeficientes ao, an, bn 

# Para calcular ao 
ao = (1/l)*(sp.integrate(y,(x,limi,lims)))
print('El valor de ao es igual a: ')
sp.pprint(ao)
print('-'*50)

# Para calcular an 
an = sp.integrate((1/l)*y*sp.cos(((w*n*x)/l)),(x,limi,lims))
print('El valor de an es igual a: ')
sp.pprint(an)
print('-'*50)

# Para calcular bn 
bn  = sp.together(sp.integrate((1/l)*y*sp.sin(((w*n*x)/l)),(x,limi,lims)))
print('El valor de bn es igual a: ')
sp.pprint(bn)
print('-'*50)


# Calculamo las serie de furier
sigma = 10
serie = ao/2
for i in range(1, sigma + 1):
    serie = serie + (an*sp.cos(((w*n*x)/l))).subs(n, i)
for j in range(1, sigma + 1):
    serie = serie + (bn*sp.sin(((w*n*x)/l))).subs(n, j)

# Mostramos la serie
print(' La serie de Fourier es igual a f(x)= ')
sp.pprint(serie)

# Mostramos la grafica
sp.plotting.plot(serie, xlim=(limi-1,lims+1))

