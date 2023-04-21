# Importante: No modificar ni el nombre ni los argumentos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

def Factorial(numero):
    '''
    Esta función devuelve el factorial del número pasado como parámetro.
    En caso de que no sea de tipo entero y/o sea menor que 1, debe retornar nulo.
    Recibe un argumento:
        numero: Será el número con el que se calcule el factorial
    Ej:
        Factorial(4) debe retornar 24
        Factorial(-2) debe retornar nulo
    '''
    #Tu código aca:
    if not isinstance(numero, int) or numero < 1:
        return None
    
    fact = 1
    for i in range(1, numero+1):
        fact *= i
    
    return fact

def EsPrimo(valor):
    '''
    Esta función devuelve el valor booleano True si el número recibido como parámetro es primo, de lo 
    contrario devuelve False..
    En caso de que el parámetro no sea de tipo entero debe retornar nulo.
    Recibe un argumento:
        valor: Será el número a evaluar
    Ej:
        EsPrimo(7) debe retornar True
        EsPrimo(8) debe retornar False
    '''
    #Tu código aca:
    if not isinstance(valor, int):
        return None
    
    if valor < 2:
        return False
    
    for i in range(2, valor):
        if valor % i == 0:
            return False
    
    return True
    
def ClaseAnimal(especie, color):
    '''
    Esta función devuelve un objeto instanciado de la clase Animal, 
    la cual debe tener los siguientes atributos:
        Edad    (Un valor de tipo de dato entero, que debe inicializarse en cero)
        Especie (Un valor de tipo de dato string)
        Color   (Un valor de tipo de dato string)
    y debe tener el siguiente método:
        CumplirAnios  (este método debe sumar uno al atributo Edad y debe devolver ese valor)
    Recibe dos argumento:
        especie: Dato que se asignará al atributo Especie del objeto de la clase Animal
        color: Dato que se asignará al atributo Color del objeto de la clase Animal
    Ej:
        a = ClaseAnimal('perro','blanco')
        a.CumplirAnios() -> debe devolver 1
        a.CumplirAnios() -> debe devolver 2
        a.CumplirAnios() -> debe devolver 3
    '''
    #Tu código aca:
    class Animal:
        def __init__(self, especie, color):
            self.Edad = 0
            self.Especie = especie
            self.Color = color

        def CumplirAnios(self):
            self.Edad += 1
            return self.Edad
    return Animal (especie, color)
    