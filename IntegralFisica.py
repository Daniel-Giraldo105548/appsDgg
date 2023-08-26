import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Definir variable simbólica
t = sp.symbols('t')

# Definir la función a integrar
func = 5 - 2*t

# Calcular la integral
integral = sp.integrate(func, t)

# Mostrar la integral
print('La integral es', integral)

# Convertir la integral simbólica a una función numérica
integral_fn = sp.lambdify(t, integral, 'numpy')

# Rango de valores para graficar
t_values = np.linspace(0, 10, 100)

# Evaluar la función integral en los valores de t
integral_values = integral_fn(t_values)

# Crear la figura y los ejes
plt.title('Integral de 5 - 2t')
plt.xlabel('t')
plt.ylabel('Valor')
plt.grid()

# Graficar la integral
plt.plot(t_values, integral_values, label='Integral de 5 - 2t')

# Mostrar la gráfica
plt.show()
