# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

def numeroCapicua(numero):
    '''
    En matemáticas, la palabra capicúa (del catalán cap i cua, 'cabeza y cola')​ 
    se refiere a cualquier número que se lee igual de izquierda a derecha que 
    de derecha a izquierda. Se denominan también números palíndromos.
    Esta función devuelve el valor booleano True si el número es capicúa, de lo contrario
    devuelve el valor booleano False 
    En caso de que el parámetro no sea de tipo entero, debe retornar nulo.
    Recibe un argumento:
        numero: Será el número sobre el que se evaluará si es capicúa o no lo es.
    Ej:
        NumeroCapicua(787) debe retornar True
        NumeroCapicua(108) debe retornar False
    '''
    #Tu código aca:
    if type (numero) != int:
        return None
    numero_str = str(numero)  
    return numero_str == numero_str[::-1]

def factorial(numero):
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
    if type(numero) != int or numero < 1:
        return None
    fact = 1
    for i in range(1, numero+1):
        fact *= i
    return fact

def proximoPrimo(actual_primo):
    '''
    Esta función devuelve el número primo siguiente al enviado como parámetro.
    En caso de que el parámetro no sea de tipo entero y/o no sea un número primo, debe retornar nulo.
    Recibe un argumento:
        actual_primo: Será el número primo a partir del cual debo buscar el siguiente
    Ej:
        ProximoPrimo(7) debe retornar 11
        ProximoPrimo(8) debe retornar nulo
    '''
    #Tu código aca:
    if not isinstance(actual_primo, int) or actual_primo <= 1:
        return None
    for i in range(2, actual_primo):
        if actual_primo % i == 0:
            return None
    for i in range(actual_primo + 1, 2 * actual_primo):
        es_primo = True
        for j in range(2, i):
            if i % j == 0:
                es_primo = False
                break
        if es_primo:
            return i
    return None

def factorizarNumero(numero):
    '''
    Esta función recibe como argumento un número entero mayor a cero y devuelva dos listas, 
    una con cada factor común y otra con su exponente, 
    esas dos listas tienen que estar contenidas en otra lista.
    En caso de que el parámetro no sea de tipo entero y/ó mayor a cero debe retornar nulo.
    Recibe un argumento:
        numero: Será el número sobre el que se hará la factorización.
    Ej:

        factorizar_numero(12) debe retornar [[2,3],[2,1]]
        factorizar_numero(13) debe retornar [[13],[1]]
        factorizar_numero(14) debe retornar [[2,7],[1,1]]
    '''
    #Tu código aca:
    if not isinstance(numero, int) or numero <= 0:
        return None
    factores = []
    exponentes = []
    i = 2
    while i * i <= numero:
        exp = 0
        while numero % i == 0:
            numero //= i
            exp += 1
        if exp > 0:
            factores.append(i)
            exponentes.append(exp)
        i += 1
    if numero > 1:
        factores.append(numero)
        exponentes.append(1)
    return [factores, exponentes]


def listaDeListas(lista):
    '''
    Esta función recibe una lista, que puede contener elementos que a su vez sean listas y
    devuelve esos elementos por separado en una lista única. 
    En caso de que el parámetro no sea de tipo lista, debe retornar nulo.
    Recibe un argumento:
        lista: La lista que puede contener otras listas y se convierte a una 
        lista de elementos únicos o no iterables.
    Ej:
        ListaDeListas([1,2,['a','b'],[10]]) debe retornar [1,2,'a','b',10]
        ListaDeListas(108) debe retornar el valor nulo.
        ListaDeListas([[1,2,[3]],[4]]) debe retornar [1,2,3,4]
    '''
    #Tu código aca:
    if not isinstance(lista, list):
        return None
    resultado = []
    for elemento in lista:
        if isinstance(elemento, list):
            resultado.extend(listaDeListas(elemento))
        else:
            resultado.append(elemento)
    return resultado

def claseVehiculo(tipo, color):
    '''
    Esta función devuelve un objeto instanciado de la clase Vehiculo, 
    la cual debe tener los siguientes atributos:
        Tipo:       Un valor dentro de los valores posibles: ['auto','camioneta','moto']
        Color:      Un valor de tipo de dato string.
        Velocidad:  Un valor de tipo de dato float, que debe inicializarse en cero.
    y debe tener el siguiente método:
        Acelerar(): Este método recibe un parámetro con el valor que debe incrementar a la
                    propiedad Velocidad y luego retornarla.
                    Si la propiedad Velocidad cobra un valor menor a cero, debe quedar en cero.
                    Si la propiedad Velocidad cobra un valor mayor a cien, debe quedar en cien.
    Recibe dos argumento:
        tipo: Dato que se asignará al atributo Tipo del objeto de la clase Vehiculo
        color: Dato que se asignará al atributo Color del objeto de la clase Vehiculo
    Ej:
        a = ClaseVehículo('auto','gris')
        a.Acelerar(10) -> debe devolver 10
        a.Acelerar(15) -> debe devolver 25
        a.Acelerar(-10) -> debe devolver 15
    '''
    #Tu código aca:
    class Vehiculo:
        def __init__(self, tipo, color):
            self.Tipo = tipo
            self.Color = color
            self.Velocidad = 0.0

        def Acelerar(self, valor):
            self.Velocidad += valor
            if self.Velocidad < 0:
                self.Velocidad = 0
            elif self.Velocidad > 100:
                self.Velocidad = 100
            return self.Velocidad

    vehiculo = Vehiculo(tipo, color)
    return vehiculo

def listaDivisibles(numero, tope):
    '''
    Esta función devuelve una lista ordenada de menor a mayor con los números divisibles 
    por el parámetro número entre uno (1) y el valor del parámetro "tope"
    Recibe dos argumentos:
        numero: Numero entero divisor
        tope: Máximo valor a evaluar a partir de uno (1)
    Ej:
        ListaDivisibles(6,30) debe retornar [6,12,18,24,30]
        ListaDivisibles(10,5) debe retornar []
        ListaDivisibles(7,50) debe retornar [7,14,21,28,35,42,49]
    '''
    #Tu código aca:
    divisibles = []
    for i in range(1, tope+1):
        if i % numero == 0:
            divisibles.append(i)
    return divisibles
    