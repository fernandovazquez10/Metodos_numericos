import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("Datos.csv")
casos = data["y"].tolist()
dia = data["x"].tolist()



dia = np.array(dia)
casos = np.array(casos)

plt.plot(dia, casos, ".")
plt.title('Casos de covid')
plt.xlabel('# Día')
plt.ylabel('# Casos')
plt.grid()
plt.show()

ln_casos = np.log(casos)

plt.plot(dia, ln_casos, ".")
plt.title('Casos de covid')
plt.xlabel('# Día')
plt.ylabel('ln(# Casos)')
plt.grid()
plt.show()


n = float(len(dia))
sumxi = float(np.sum(dia))
sumyi = float(np.sum(ln_casos))
sumxiyi = float(np.sum(dia * ln_casos))
sumxi2 = float(np.sum( dia**2 ))
xmed = np.mean(dia) 
ymed = np.mean(ln_casos)

a1 = (n*sumxiyi - (sumxi*sumyi))/(n*sumxi2 - (sumxi**2))
a0 = ymed - a1*xmed

x = np.linspace(0, n, 60)
y = a0 + a1*x

plt.plot(x, y, color="black")
plt.plot(dia, ln_casos, ".")
plt.title('Casos de covid')
plt.xlabel('# Día')
plt.ylabel('ln(# Casos)')
plt.grid()
plt.show()

yor = np.exp(a0)*np.exp(a1*x)

plt.plot(x, yor, color="black")
plt.plot(dia, casos, ".")
plt.title('Casos de covid')
plt.ylim(0,500000)
plt.xlabel('# Día')
plt.ylabel('# Casos')
plt.grid()
plt.show()
alfa = np.exp(a0)
print(f"La ecuación es: {alfa}*{a1}**x")

print("alfa: ", np.exp(a0))
print("beta: ", a1)