from Steffensen_Root import SteffensenRoot # Importamos la funcion desde otro programa
import sympy as sp

variable = "x"
x = sp.Symbol(variable)
a = ((x-2)**2)-sp.log(x) # Definimos la funcions que vamos a encontrar

# Se realiza el metodo para la primera raiz
print("Primer raiz")
SteffensenRoot(a,0.8,25,12)

# Se realiza el metodo para la segunda raiz 
print("Segunda raiz")
SteffensenRoot(a,3.5,25,12)
