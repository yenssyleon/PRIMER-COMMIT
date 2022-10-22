#Hola, este es un código, para hacer mi primer commit, qué emoción.
#Se me ocurre hacer un convertidor de grados a radianes :)

import math 

print("main.pyESTA ES UNA CALCULADORA PARA CONVERTIR GRADOS A RADIANES :)")

#Sí sirve:)

print("Ingrese los grados:)")
getgrades=int(input())

class CalculadoraGR:
    def Calculadora(self,getgrades):
        rad=getgrades*(math.pi/180)
        return rad

radian=CalculadoraGR()
resultado=radian.Calculadora(getgrades)

print("el ángulo en radianes es:")
#Vamos a dejar un espacio para que se vea bonito
#Aunque en la consola no se ve bonito :p
print(resultado)
