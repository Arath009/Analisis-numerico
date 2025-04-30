# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 14:29:27 2025

@author: Msi Mem
"""
import sys
from numpy import sign
from math import sin,cos,tan
import math
import numpy as np
from numpy import sign
import matplotlib.pyplot as plt
from math import *

# =============================================================================
# PREGUNTA 1
# =============================================================================

def newtonRaphson(f,df,a,b,tol=1.0e-9):
  fa = f(a)
  if fa == 0: return a
  fb = f(b)
  if fb == 0: return b
  if sign(fa) == sign(fb): err('La raiz no esta en el intervalo')
  x = 0.5*(a + b)
  for i in range(30):
    print(i)
    fx = f(x)
    if fx == 0.0: return x 
    if sign(fa) != sign(fx): b = x # Haz el intervalo mas pequeño
    else: a = x
    dfx = df(x)  
    try: dx = -fx/dfx # Trata un paso con la expresion de Delta x
    except ZeroDivisionError: dx = b - a # Si division diverge, intervalo afuera
    x = x + dx # avanza en x
    if (b - x)*(x - a) < 0.0: # Si el resultado esta fuera, usa biseccion
      dx = 0.5*(b - a)
      x = a + dx 
    if abs(dx) < tol*max(abs(b),1.0): return x # Checa la convergencia y sal
  print('Too many iterations in Newton-Raphson')


def f(x): return x**3 - 75
def df(x): return 3*x**2

root = newtonRaphson(f, df, 3, 5, tol=1.0e-4)
print('Raíz cúbica de 75 ≈', round(root, 4))




# =============================================================================
# EJERCICIO 2
# =============================================================================


    

### GRAFICAR PARA VER DONDE LA FUNCION ES 0 Y ELEGIR MIS LIMITES ####


def f(x):
    return x**3 - 3.23*x**2 - 5.54*x + 9.84


x_vals = np.linspace(-2, 4, 1000)  
y_vals = f(x_vals)


plt.plot(x_vals, y_vals, label=r'$x^3 - 3.23x^2 - 5.54x + 9.84$', color='blue')
plt.axhline(0, color='black', linewidth=1)  # Línea horizontal en y=0
plt.axvline(0, color='black', linewidth=1)  # Línea vertical en x=0
plt.grid(True)
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfica de la función')


plt.show()




def y(x):                    # define la funcion y(x)
  y =x**3 - 3.23*x**2 - 5.54*x + 9.84
  return y

x1 = 1 # peticion de valor x1
x2 = 2 # peticion de valor x2
y1 = y(x1)                                    # evalua la funcion y(x1)
y2 = y(x2)                                    # evalua la funcion y(x1)

if y1*y2 > 0:                                 # prueba si los signos son iguales
  print('No hay raices en el intervalo')
  exit

for i in range(100):
  xh = (x1+x2)/2
  yh = y(xh)                                  # evalua la funcion y(xh)
  y1 = y(x1)                                  # evalua la funcion y(x1)
  if abs(y1) < 1.0e-6:
    break
  elif y1*yh < 0:
    x2 = xh
  else:
    x1 = xh
print('La raiz es: %.5f' % x1)
print('Numero de bisecciones: %d' % (i+1))

print('La raíz más pequeña es: %.5f' % x1)
print('Número de iteraciones realizadas: %d' % i)


# =============================================================================
# EJERCICIO 3
# =============================================================================





#Diferencias finitas

"Con aproximacion de diferencias finitas: primeras centrales tenemos que:"  
"f'(x)=[f(x+h) - f(x) / h]"

x = [2.36, 2.37, 2.38, 2.39]
fx= [0.85866, 0.86289, 0.86710, 0.87129]
h = x[1] - x[0]  

df=(fx[1] - fx[0])/h
print("la derivada de f(2.36) es",df)

#SEGUNDA DERIVADA

"f''(x+2*h)-2*f(x+h)+f(x))/(h**2)"

d2f=(fx[2]-2*fx[1]+fx[0])/(h**2)
print("la segunda derivada de f(2.36) es", d2f)


# =============================================================================
# EJERCICIO 4
# =============================================================================



"""):"""
