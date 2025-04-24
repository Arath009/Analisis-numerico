# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 13:02:32 2025

@author: Msi Mem
"""

# =============================================================================
##############################   SECCION 4.1. #################################
# =============================================================================


# =============================================================================
#EJERCICIO 11
# =============================================================================

#Escribe un programa que calcule todas las raíces de f(x) = 0
#Prueba el programa encontrando las raíces de 𝑥sin⁡𝑥 + 3cos𝑥 − 𝑥=0 en el intervalo (−6,6).

## Modulo Newton-Raphson
## raiz = newtonRaphson(f,df,a,b,tol=1.0e-9).
## Encuentra la raiz de f(x) = 0 combinando Newton-Raphson
## con biseccion. La raiz debe estar en el intervalo (a,b).
## Los usuarios definen f(x) y su derivada df(x).


import sys
from numpy import sign
from math import sin,cos,tan
import math
import numpy as np
from numpy import sign
import matplotlib.pyplot as plt
from math import *


def err(string):
  print(string)
  input('Press return to exit')
  sys.exit()

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
  
def f(x): return x*sin(x)+3*cos(x)-x
def df(x): return x * cos(x) - 2 * sin(x) - 1
root = newtonRaphson(f,df,-6.0,6.0)
print('Root =',root)


print("\n")
print("EJERCICIO 19")


# =============================================================================
# EJERCICIO 19
# =============================================================================

#La velocidad 𝑣 de un cohete Saturno V en vuelo vertical cerca de la superficie 
#de la Tierra puede ser aproximada por:

    
from sympy import symbols, ln, pretty

u, M0, m_dot, t, g = symbols('u M0 m_dot t g')


v = u * ln(M0 / (M0 - m_dot * t)) - g * t

print("La velocidad v puede aproximarse por:")
print(pretty(v))


u = 2510  # m/s
M0 = 2.8e6  # kg
m = 13.3e3  # kg/s
g = 9.81  # m/s^2
v_target = 335  # m/s


def ridder(f,a,b,tol=1.0e-9):
  fa = f(a)
  if fa == 0.0: return a
  fb = f(b)
  if fb == 0.0: return b
  if sign(fa)!= sign(fb): c=a; fc=fa
  for i in range(30):
# Compute the improved root x from Ridder’s formula
      c = 0.5*(a + b); 
      fc = f(c)
      s = math.sqrt(fc**2 - fa*fb)
      if s == 0.0: return None
      dx = (c - a)*fc/s
      if (fa - fb) < 0.0: dx = -dx
      x = c + dx; fx = f(x)
# Test for convergence
  if i > 0:
     xOld = x
     if abs(x - xOld) < tol*max(abs(x),1.0): return x
# Re-bracket the root as tightly as possible
  if sign(fc) == sign(fx):
    if sign(fa)!= sign(fx): b = x; fb = fx
    else: a = x; fa = fx
  else:
    a = c; b = x; fa = fc; fb = fx
  return None
  print('Too many iterations')
  

  
def f(t):
    u = 2510  # m/s
    M0 = 2.8e6  # kg
    m = 13.3e3  # kg/s
    g = 9.81  # m/s^2
    v_target = 335  # m/s
    return u * math.log(M0 / (M0 - m *t)) - g*t - v_target

# Buscar la raíz en el intervalo (a, b)
a = 70
b = 71
root = ridder(f, a, b)
print(f"El tiempo en que el cohete alcanza la velocidad del sonido es aproximadamente: {root:.6f} segundos.")



t = np.linspace(70, 75, 1000)
v = u * np.log(M0 / (M0 - m * t)) - g * t - v_target

ax = plt.subplot(111)
line, = plt.plot(t, v, lw=2)


plt.annotate('Raíz', xy=(70.8,2.0), xytext=(70.8,40.0),
             arrowprops=dict(facecolor='black', shrink=0.05),
             )

plt.grid(True)
plt.ylim(-50, 50)
plt.title("v(t) = u * ln(M0 / (M0 - m * t)) - g * t - v_target")
plt.ylabel("v(t) - Velocidad (m/s)")
plt.xlabel("Tiempo (s)")

print("\n")
print("SECCION 5.1\nEJERCICIO 9")
# =============================================================================
############################3 SECCION 5.1 ######################################
# =============================================================================



# =============================================================================
# EJERCICIO 9
# =============================================================================

#Usa los datos de la tabla para calcular 𝑓'(0.2) con la mayor precisión posible

"""
Con aproximacion de diferencias finitas: primeras centrales tenemos que:
f'(x)=[f(x+h) - f(x-h) / 2h]

y sabemos que h=0.1
"""
x=[0,0.1,0.2,0.3,0.4]
fx=[0.000000,0.078348,0.138910,0.192916,0.244981]
h=0.1

df=(fx[3]-fx[1])/2*h
print("la derivada de f(0.2) es",df)




print("\nEJERCICIO10")
# =============================================================================
# EJERCICIO 10
# =============================================================================

"""
Usando cinco cifras significativas en los cálculos, determina d(sin(x))/dx en x = 0.8
mediante:
(a) la primera aproximación por diferencia forward.
(b) la primera aproximación por diferencia centrada.

En cada caso, utiliza h que proporcione el resultado más preciso (esto requiere experimentación).
"""


#Diferencias finitas


def f(x,n): #La función a derivar con n decimales
  return round(sin(x),n)

def dff(x,h,f,n): #primera derivada de f con aproximación forward con n decimales
  dff=(f(x+h,n)-f(x,n))/h
  return dff

def dfc(x,h,f,n): #primera derivada de f con aproximación central con n decimales
  dfc=(f(x+h,n)-f(x-h,n))/(2*h)
  return dfc


#Primera derivada de f con aproximación forward
h=0.25
print("Con la aproximación forward tenemos que")
print("  h        5 dígitos   Error    ")
print("------------------------------------------------------")
for i in range(10):
  E1=abs(((f(0.8,6)-dff(0.8,h,f,5))/f(0.8,5))*100)
  
  print("%.5f   %.5f    %.2f"      %(h,dff(0.8,h,f,5),E1))
  h=h/2
print()

print("basandonos en el error, el resultado mas preciso es  0.69632\n")





h=0.10
print("Con la aproximación central tenemos que")
print("  h        5 dígitos   Error    ")
print("------------------------------------------------------")
for i in range(10):
  E1=abs(((f(0.8,6)-dfc(0.8,h,f,5))/f(0.8,5))*100)
  
  print("%.5f   %.5f    %.2f"      %(h,dfc(0.8,h,f,5),E1))
  h=h/2
print()

print("basandonos en el  error, el resultado mas preciso es: 0.70400\n")



print("\nSECCION 6.1\n EJERCICIO 1 ")
# =============================================================================
# SECCION 6.1
# =============================================================================

"""Usa la regla trapezoidal recursiva para evaluar la integral 
definida de 0 a pi/4 de la funcion ln(1 + tan(x))"""

def trapecio_recursiva(f,a,b,Iold,k):
  if k == 1: Inew = (f(a) + f(b))*(b - a)/2.0
  else:
    n = 2**(k -2 ) # numero de nuevos puntos
    h = (b - a)/n # espaciamiento de nuevos puntos
    x = a + h/2.0
    sum = 0.0
    for i in range(n):
      sum = sum + f(x)
      x = x + h
      Inew = (Iold + h*sum)/2.0
  return Inew

def f(x): return math.log(1+tan(x)) 
Iold = 0.0
for k in range(1,21):
  Inew = trapecio_recursiva(f,0.0,math.pi/4,Iold,k)
  if (k > 1) and (abs(Inew - Iold)) < 1.0e-6: break
  Iold = Inew

print('Integral =',Inew)
print('n Panels =',2**(k-1))

