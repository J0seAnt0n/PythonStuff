# Importar las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
from celluloid import Camera
from mpl_toolkits.mplot3d import Axes3D

# Crear el set de datos
n = 100 # Número de puntos de datos
x = np.random.uniform(-10, 10, n) # Coordenadas x
y = np.random.uniform(-10, 10, n) # Coordenadas y
z = np.random.uniform(-10, 10, n) # Coordenadas z
roll = np.random.uniform(0, 2*np.pi, n) # Ángulo de rotación alrededor del eje x
pitch = np.random.uniform(0, 2*np.pi, n) # Ángulo de rotación alrededor del eje y
yaw = np.random.uniform(0, 2*np.pi, n) # Ángulo de rotación alrededor del eje z

# Crear la figura y el eje 3D
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Crear el objeto de cámara
camera = Camera(fig)

# Crear la animación del dron
for i in range(n):
    # Borrar el eje
    ax.clear()
    # Establecer los límites del eje
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_zlim(-10, 10)
    # Establecer las etiquetas del eje
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    # Crear la matriz de rotación
    R = np.array([[np.cos(yaw[i])*np.cos(pitch[i]), np.cos(yaw[i])*np.sin(pitch[i])*np.sin(roll[i])-np.sin(yaw[i])*np.cos(roll[i]), np.cos(yaw[i])*np.sin(pitch[i])*np.cos(roll[i])+np.sin(yaw[i])*np.sin(roll[i])],
                  [np.sin(yaw[i])*np.cos(pitch[i]), np.sin(yaw[i])*np.sin(pitch[i])*np.sin(roll[i])+np.cos(yaw[i])*np.cos(roll[i]), np.sin(yaw[i])*np.sin(pitch[i])*np.cos(roll[i])-np.cos(yaw[i])*np.sin(roll[i])],
                  [-np.sin(pitch[i]), np.cos(pitch[i])*np.sin(roll[i]), np.cos(pitch[i])*np.cos(roll[i])]])
    # Crear los vectores unitarios del dron
    u = np.array([1, 0, 0]) # Vector unitario en el eje x
    v = np.array([0, 1, 0]) # Vector unitario en el eje y
    w = np.array([0, 0, 1]) # Vector unitario en el eje z
    # Rotar los vectores unitarios según la orientación del dron
    u = R.dot(u)
    v = R.dot(v)
    w = R.dot(w)
    # Escalar los vectores unitarios para visualizarlos mejor
    s = 2 # Factor de escala
    u = u * s
    v = v * s
    w = w * s
    # Dibujar el dron como un punto y sus ejes como flechas
    ax.scatter(x[i], y[i], z[i], c='r', marker='o') # Punto
    ax.quiver(x[i], y[i], z[i], u[0], u[1], u[2], color='b') # Flecha del eje x
    ax.quiver(x[i], y[i], z[i], v[0], v[1], v[2], color='g') # Flecha del eje y
    ax.quiver(x[i], y[i], z[i], w[0], w[1], w[2], color='k') # Flecha del eje z
    # Tomar una foto del cuadro
    camera.snap()

# Crear el objeto de animación
animation = camera.animate()

# Mostrar la animación
plt.show()
