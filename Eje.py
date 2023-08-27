import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# Definir las variables simbólicas
t = sp.symbols('t')

# Definir la función a integrar
func = sp.sqrt(t) + 4

# Calcular la integral indefinida
integral = sp.integrate(func, t)

# Convertir la integral simbólica a una función numérica
integral_fn = sp.lambdify(t, integral, 'numpy')

# Definir un rango de valores de t para graficar
t_values = np.linspace(0, 10, 400)

# Evaluar la función 
integral_values = integral_fn(t_values)

# Crear la figura y los ejes
plt.figure(figsize=(10, 6))
plt.title('Función ')
plt.xlabel('t')
plt.ylabel('Valor')
plt.grid()

# Graficar la función original y su integral
plt.plot(t_values, integral_values)
plt.legend()

# Mostrar la gráfica
plt.show()

