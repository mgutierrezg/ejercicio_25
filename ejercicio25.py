import numpy as np
import matplotlib.pyplot as plt

#DATOS TOMADOS DE WIKIPEDIA

G = 6.674*(10**-11)
masasol = 1.989*(10**30)
velocidadmercurio = 47872.5
velocidadtierra = 29785.9
velocidadjupiter = 13069.7
distanciamercurio = 5790917500
distanciatierra = 14959787000
distanciajupiter = 77841201000
rangoalfa = np.linspace(0,4,1000)

#FUNCION BETA
def beta(v, r, alfa):
    bet = (v*v)/(r**(1-alfa))
    return bet


y = beta(velocidadmercurio, distanciamercurio, rangoalfa)
    
plt.plot(rangoalfa,y)
plt.savefig("mercurio.pdf")
plt.show()
