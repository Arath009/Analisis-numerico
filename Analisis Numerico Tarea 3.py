# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 11:06:28 2025

@author: Msi Mem
"""
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from math import *

#EJERCICIO 1

# Definir los puntos
x = [0, 21.1, 37.8, 54.4, 71.1, 87.8, 100]
y = [0.101, 1.79, 1.13, 0.696, 0.519, 0.338, 0.296 ]
m = len(x)
n = m - 1

# Función para calcular los polinomios básicos de Lagrange
def lagrange_basis(xp, x_points, i):
    L_i = 1
    for j in range(len(x_points)):
        if j != i:
            L_i *= (xp - x_points[j]) / (x_points[i] - x_points[j])
    return L_i


def lagrange_interpolation(xp, x_points, y_points):
    yp = 0
    for i in range(len(x_points)):
        yp += y_points[i] * lagrange_basis(xp, x_points, i)
    return yp
# Solicitar el valor de x para interpolar
xp = [10,30,60,90]
yp = [0,0,0,0]
for i in range(len(xp)):
    yp[i] = lagrange_interpolation(xp[i], x, y)
    print("For x = %.1f, y = %.1f" % (xp[i], yp[i]))

# Crear puntos para la interpolación
x_interpolado = np.linspace(min(x), max(x), 100)
y_interpolado = [lagrange_interpolation(x_val, x, y) for x_val in x_interpolado]
# Graficar los puntos originales
plt.scatter(x, y, label="Puntos Originales", color="red")
# Graficar el polinomio de interpolación de Lagrange
plt.plot(x_interpolado, y_interpolado, label="Interpolación de Lagrange", linestyle="-")
# Graficar los puntos de interpolación
plt.scatter(xp, yp, label="Punto Interpolado", color="black", zorder=5)


# Añadir etiquetas y leyenda
plt.xlabel("T(°C)")
plt.ylabel("μk(10^-3 m^2/s)")
plt.title("Polinomio de Interpolación de Lagrange")
plt.legend()
plt.grid(True)

# Mostrar la gráfica
plt.show()

# =============================================================================
# EJERCICIO 2
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp


def lagrange_1(x_points, y_points, xp):
    """
    Calcula y grafica el polinomio de interpolación de Lagrange.

    Parámetros:
    x_points (list or array): Puntos en el eje x.
    y_points (list or array): Puntos en el eje y.
    xp (float): Punto en el que se desea interpolar.

    Retorna:
    yp (float): Valor interpolado en xp.
    """
    m = len(x_points)
    n = m - 1
    # Definir la variable simbólica
    x = sp.symbols("x")

    # Función para calcular los polinomios básicos de Lagrange
    def lagrange_basis(xp, x_points, i):
        L_i = 1
        for j in range(len(x_points)):
            if j != i:
                L_i *= (xp - x_points[j]) / (x_points[i] - x_points[j])
        return L_i

    # Función para calcular el polinomio de Lagrange
    def lagrange_interpolation(xp, x_points, y_points):
        yp = 0
        for i in range(len(x_points)):
            yp += y_points[i] * lagrange_basis(xp, x_points, i)
        return yp

    # Calcular el valor interpolado
    yp = lagrange_interpolation(xp, x_points, y_points)
    print("For x = %.1f, y = %.1f" % (xp, yp))

    # Crear puntos para la interpolación
    x_interpolado = np.linspace(min(x_points), max(x_points), 100)
    y_interpolado = [
        lagrange_interpolation(x_val, x_points, y_points) for x_val in x_interpolado
    ]

    # Graficar los puntos originales
    plt.scatter(x_points, y_points, label="Puntos Originales", color="red")

    # Graficar el polinomio de interpolación de Lagrange
    plt.plot(
        x_interpolado, y_interpolado, label="Interpolación de Lagrange", linestyle="-"
    )

    # Graficar el valor interpolado
    plt.scatter(xp, yp, color="black", zorder=5)
    plt.text(xp, yp, f"({xp:.1f}, {yp:.1f})", fontsize=12, verticalalignment="bottom")

    # Añadir etiquetas y leyenda
    plt.xlabel("h(km)")
    plt.ylabel("p")
    plt.title("Polinomio de Interpolación de Lagrange")
    plt.legend()
    plt.grid(True)

    # Mostrar la gráfica
    plt.show()

    # Construir el polinomio de interpolación simbólicamente
    polinomio = 0
    for i in range(len(x_points)):
        term = y_points[i]
        for j in range(len(x_points)):
            if j != i:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        polinomio += term

    # Simplificar el polinomio
    polinomio_simplificado = sp.simplify(polinomio)

    # Imprimir el polinomio de interpolación
    print("Polinomio de Interpolación de Lagrange:")
    print(f"y(x) = {polinomio}")
    print("\nPolinomio Simplificado:")
    print(f"y(x) = {polinomio_simplificado}")

    return yp
try:
    x_points = [0,1.525,3.050,4.575,6.10,7.626,9.150]
    y_points = [1,0.8617,0.7385,0.6292,0.5328,0.4481,0.3741]
    xp = float(input("Enter x: "))
    lagrange_1(x_points, y_points, xp)
except ValueError:
    print("Please insert a valid number")
    
    
    
    
# =============================================================================
# EJERCICO 3
# =============================================================================


def evalPoly(a, xData, x):  # Función que evalua polinomios de Lagrange
    n = len(xData) - 1  # Grado del polinomio
    p = a[n]
    for k in range(1, n + 1):
        p = a[n - k] + (x - xData[n - k]) * p
    return p


def coeffts(xData, yData):
    m = len(xData)  # Número de datos
    a = yData.copy()
    for k in range(1, m):
        a[k:m] = (a[k:m] - a[k - 1]) / (xData[k:m] - xData[k - 1])
    return a

xData = np.array([0,400,800,1200,1600])
yData = np.array([0,0.072,0.233,0.712,3.400])
coeff = coeffts(xData, yData)
x = np.arange(0, 2550, 100)
plt.plot(x, evalPoly(coeff, xData, x), "b", label="Newton")
plt.plot(xData, yData, "o", label="Datos", color="black")
plt.xlabel('V (rpm)')
plt.ylabel('A (mm)')
plt.legend()
plt.grid()
plt.show()

print("  x    yExacta        yInt       Error(%)")
print("------------------------------------------")
for i in range(len(x)):
    y = evalPoly(coeff, xData, x[i])
    yExacta = 4.8 * cos(pi * x[i] / 20)
    Error = abs(((yExacta - y) / yExacta) * 100)
    print(" %.1f  %.8f   %.8f    %.8f" % (x[i], yExacta, y, Error))