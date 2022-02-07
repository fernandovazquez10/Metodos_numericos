"""
Datos de la funcion 
deltap = caida de presion
p = densidad del fluido
Go = velocidad masica
Dp = diametro de las particulas en el cauce
M = Viscosidad del fluido 
L = Longitud del lecho
E = es la fraccion del cauce

Considerando 
 Sustituimos los terminos que se nos dan del problema 
 para mantener un estilo mas pytonico 
"""
# Utilizaremos la libreria sympy para
# graficar la funcion y volver simbolos la variable y funcion
import sympy as sp



# variable = input("Ingrese la variable sobre la que guste trabajar: ")
variable = "E" #Como ya contamos con la variable, se escribe en el codigo

E = sp.Symbol(variable) 

# ec = input("Ingrese la ecuacion por favor: ")
ec = 10*((E**3)/(1-E))-(150*((1-E)/1000))+1.75 #De igual manera con la funcion

y = sp.sympify(ec)

print(y)
ejey = 'f(' + variable + ')'
# Mostrar la gráfica
sp.plotting.plot(y, (E,0,1.25) , xlabel = variable, ylabel = ejey)

"""
En caso de querer ingresar los datos desde la terminal
Usar esta seccion 

# Se solicita los valores a y b, hasta que sean validos. 
while True:
    a = float(input("Ingrese el límite inferior a: "))
    b = float(input("Ingrese el límite inferior b (> a): "))
    # Se verifica que el intervalo sea vallido
    # Y contenta una raiz
    if (a < b) and ( (float(y.subs(x,a).evalf())*float(y.subs(x,b).evalf())) < 0 ):
        break
"""
# De la grafica determinamos este intervalo
a = .6
b = 1.2   
    
# Colocamos la presicion deseada
d = int(12)
p  = float(1/(10**12))

# Iniciamos un contador 
i = 1
# Creamos  un error inicial parcial
er = (b-a)/2 
# Empezamos a realizar el metodo
print("{:12}\t{:12}\t{:12}\t{:12}\t{:12}".format('i','a','b','m','er'))
while i < 45 and er > p :
    m = (a+b)*.5 
    leyenda = "{:}\t{:12}\t{:12}\t{:12}\t{:12}".format(i,round(a,d),round(b,d),round(m,d),round(er,d))
    print(leyenda)

    if( float(y.subs(E,a).evalf())*float(y.subs(E,m).evalf()) < 0):
        # a se mantiene & b pasa a ser m
        a = a
        b = m
        
    elif( float(y.subs(E,m).evalf())*float(y.subs(E,b).evalf()) < 0):
        # a ahora será m & b se mantiene
        a = m
        b = b
    er =(b-a) / 2
    i += 1
print("La raíz a {:} dígitos de precisión es: {:}".format(d, round(m,d)))
    
  