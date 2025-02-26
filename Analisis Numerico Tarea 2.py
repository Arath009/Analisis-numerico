# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 00:14:15 2025

@author: Msi Mem
"""
import numpy as np
#EJERCICIO 1: Interseccion de trayectorias

print("EJERCICIO 1: ENCUENTRE LOS PUNTOS DE INTERSECCION DE LOS OBJETOS")

#Matriz
a=np.array([[2,-1,3],
            [0,2,-1],
            [7,-5,0]])

#Matriz solucion
b=np.array([24,14,6])

Intr=np.linalg.solve(a, b)

x,y,z=Intr
print("El punto de interseccion sera:x=",x,"y=",y,"z=",z)


#EJERCICIO 2: CARGA DE LOS QUARKS
print("\n EJERCICIO 2: Determine la carga de los quarks")

#Matrices de proton y neutron con sus respectivos quarks
qrks=np.array([[2,1],
           [1,2]])

#Matriz solucion con las respectivas cargas de las particulas
carga=np.array([1,0])

cargas=np.linalg.solve(qrks, carga)

up,dw=cargas
print("La carga del quark up es=",up,"\nla carga del quark down es=",dw)


#EJERCICIO 3
print("\n EJERCICIO 3: Determine la cantidad de meteoros de determinadas masas que entran a la atmosfera")


#   Matriz
A = np.array([
     [1, 1, 1, 1],
     [1, 5, 10, 20],  
     [0, 1, -4, 0],   
     [1, -2, 0, 0]    
])

# Matriz solucion
b = np.array([26, 95, 0, -1])

met = np.linalg.solve(A, b)

x1, x5, x10, x20 = met

print(f'Cantidad de meteoros de 1 kg: {x1}')
print(f'Cantidad de meteoros de 5 kg: {x5}')
print(f'Cantidad de meteoros de 10 kg: {x10}')
print(f'Cantidad de meteoros de 20 kg: {x20}')

