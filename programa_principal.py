import sys
sys.path.append('C:\\Users\\PC\\Desktop\Curso js\\Mis modulos')
from mi_modulo import Saludar
from mi_modulo import Calculadora 
pedirnombre= input('podria decirme su nombre:')
nombre= Saludar(pedirnombre)
print(nombre)

a= float(input('Dijite el primer valor de la operación:'))
b= float(input('Dijite el primer valor de la operación:'))
operacion= input('Ingresa la operación (suma, resta, multiplicacion, division, porcentaje)')
resultado = Calculadora(a, b, operacion)
print(resultado)
