import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots() #iniciando la grafica
xdata, ydata = [], [] # Forma de inicializar los datos X Y
ln, = plt.plot([],[], 'ro') # Ro puntos rojos 

def init(): #nombre tal cual obligatorio sin argumentos
    ax.set_xlim(0, 6*np.pi) # Limites de X 360°
    ax.set_ylim(-1.5,1.5) # Limites de Y por que es sen
    return ln,

def update(frame):  # Actualizando cada uno de los puntos
    xdata.append(frame) # Agregando para X
    ydata.append(np.sin(frame)) # Usamos sen
    ln.set_data(xdata,ydata) # datos ya generados (x,y)
    return ln,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 6*np.pi, 50),
                   interval=100, init_func=init, blit=True)  
plt.show()
