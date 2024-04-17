def Saludar(nombre):
    return f' Hola, {nombre}'

def Calculadora(a, b, operacion):
    if operacion == 'suma':
        resultado = a + b
    elif operacion == 'resta':
        resultado = a - b
    elif operacion == 'multiplicacion':
        resultado = a * b
    elif operacion == 'division':
        resultado = a / b
    elif operacion == 'porcentaje':
        resultado = (a * b) / 100
    else:
        return 'Operación no válida'

    return f'El resultado es: {resultado}'






