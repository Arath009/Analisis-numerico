# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 22:50:12 2025

@author: Msi Mem
"""

import math
import cmath
import numpy as np
from math import tan, cos
import sympy as sp
"""
#EJERCICIO 1: Convertir de Fahrenheit a Celsius.
print("EJERCICIO 1: CONVERTIR DE GRADOS FARENHEIT A CELSIUS")
far=float(input("Ingrese la temperatura en grados Fahrenheit: "))
cels=(far-32)* 5/9
print("La temperatura en grados Celsius es:", round(cels,2), "°C")


#EJERCICIO 2: Calcular la funcion sinh de 2pi de 3 distintas maneras
print("EJERCICIO 2: Calcular la funcion sinh de 2pi de 3 distintas maneras")
print("Calcular el seno hiperbolico de 2 pi")
 #Calculando directamente el sinh
x=2*math.pi
a=math.sinh(x)
print("El seno hiperbolico de 2*PI es:",a)

 #Evaluando con la definición del lado derecho, usando la función exponencial
print("Evaluar el lado derecho de la ecuacion con la funcion exponencial")
b=(math.e**x - math.e**-x)/2
print("La ecuacion es igual a:",b)

#Evaluando con la definición del lado derecho, usando la potencia
print("Evaluando el lado derecho de la ecuacion con la potencia")
c=(math.exp(x)- math.exp(-x))/2
print("La ecuacion es igual a:",c)


#EJERCICIO 3
print("EJERCICIO 3:Calcular el valor de SEN(i*x) y de i_SENH(X) para comprobar la identidad:")

x=complex(int(input("Ingrese un numero cualquiera:")))

s=cmath.sin(1j*x)
print("el seno de",x,"es:",s)
sh=complex(cmath.sinh(x))
print(" el i_senh de x es:",sh,"\n como el Seno(ix) = iSeno hiperbolico(x) la propiedad se cumple")

print("Ahora calcular el valor de Coseno(x), iSeno(x) y de e^ix para ciertos valores dados de x para verificar la identidad")

y=complex(int(input("Ingrese un numero cualquiera:")))
c=cmath.cos(y)
print("el coseno de",y,"es:",c)
s=1j*(cmath.sin(y))
print("el i_seno(x) es:",s)
exp=1j*y
e=cmath.exp(exp)
print("el valor de e elevado a",y,"i, es:",e)
print("Ahora sumamos el resultado de las funciones Coseno(x) + iSeno(x)")
e2=c+s
print("Como el valor de coseno(X)+isen(x) es:",e2,"\n Y el valor de e^ix es:",e,"\nla propiedad se cumple")


#EJERCICIO 4: elabora un programa en el que uses Numpy para calcular el valor de las raices con diferentes valores de a b y c  para obtener ejemplos de raices reales y complejas.
print("EJERCICIO 4: elabora un programa en el que uses Numpy para calcular el valor de las raices con diferentes valores de a b y c  para obtener ejemplos de raices reales y complejas")
a=float(input("Ingrese un valor para a:"))
b=float(input("Ingrese un valor para b:"))
c=float(input("Ingrese un valor para c:"))
discriminante= (b**2) - (4*a*c)
if discriminante>=0:
    x1=(-b + np.sqrt(discriminante))/(2*a)
    x2=(-b - np.sqrt(discriminante))/(2*a)
    print("sus resultados son valores reales\n z1:",x1,"\n z2:",x2)
else:
    x1=(-b + np.sqrt(discriminante + 0j))/(2*a)
    x2=(-b - np.sqrt(discriminante + 0j))/(2*a)
    print("su resultados son valores complejos\n z1:",x1,"\n z2:",x2)
  
"""
#EJERCICIO 5: En tu portafolio de clase, elabora un programa en el que evalues esta expresión. 
#El programa debe escribir el valor de todas las variables involucradas junto con las unidades usadas.#
print("EJERCICIO 5: En tu portafolio de clase, elabora un programa en el que evalues la altura de una pelota en funcion de x con la ecuacion de la trayectoria" )
#DEFINIR LAS VARIABLES
#Variables de la funcion
theta=float(input("Ingrese un valor para theta:"))
v=float(input("Ingrese un valor para la rapidez inicial:"))
y=float(input("Ingrese un valor para la posicion inicial:"))
x=float(input("Ingrese el valor de x para evaluar la funcion:"))
g=float(9.91)

#ECUACION DE LA TRAYECTORIA
yx = (x * math.tan(theta)) - (g / (2 * (v**2))) * ((x**2)/( math.cos(theta)**2)) + y

print("v0=",v,"m/s\nθ=",theta,"°\ng=",g,"m/s^2\ny0=",y,"m\nx=",x,"m")

print("la altura de la pelota cuando x=",x,"es:",yx,"m")

