from typing import List, Union

###############################################################################

# Comparo los dos primeros elementos de la tupla
# Vuelvo a llamar a la funcion enviando como parametros:
# el mayor elemento, de los dos evaluados, en la posición cero 
# y los elementos sin evaluar 
# finaliza cuando quede un unico elemento

def maximo_recursivo(*args) -> float:
    if len(args)==1: #Si hay un unico argumento lo retorna
        return args[0]
    else: #Si hay mas de un arg comparo
        if args[1] > args[0]: #Si el segundo (posición 1) arg es mayor al primero (posición 0)
            return maximo_recursivo(*args[1:]) #llamo a la funcion enviando los args sin el primer elemento
        else: #Si el primer elemento (posición 0) es mayor al segundo (posición 1)
            return maximo_recursivo(args[0],*args[2:]) #llamo a la funcion enviando los arg sin el segundo elemento
    
"""Toma una cantidad arbitraria de números y devuelve el mayor.

    Restricciónes:
        - No utilizar la función max
        - No utilizar la ninguna otra función salvo maximo_recursivo
        - Resolver de manera recursiva
"""

# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert maximo_recursivo(1, 10, 5, -5) == 10
    assert maximo_recursivo(4, 9, 18, 6) == 18
    assert maximo_recursivo(24, 9, 18, 20) == 24
    assert maximo_recursivo(24, 9, 18, 30) == 30
# NO MODIFICAR - FIN


###############################################################################


from functools import reduce  # noqa: E402


def sumatoria_reduce(n: int) -> int:
    lista=[]
    for i in range(1,n+1):
        lista.append(i)
    return reduce(lambda x,y: x + y, lista)
    """Devuelve la suma de los números de 1 a N.

    Restricción: Utilizar la función reduce.
    Referencia: https://docs.python.org/3/library/functools.html#functools.reduce  # noqa: E501
    """


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert sumatoria_reduce(1) == 1
    assert sumatoria_reduce(100) == 5050
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_sorted(lista: List[Union[float, str]]) -> List[Union[float, str]]:  # noqa: E501
    nueva = sorted(lista, key = lambda x: type(x) is int)
    return nueva
    """Re-escribir utilizando la función sorted con una custom key.

    Restricciones:
        - No utilizar bucles.
        - No utilizar comprensiones.
        - Utilizar un lambda.

    Referencia: https://docs.python.org/3/library/functions.html#sorted
    """


# NO MODIFICAR - INICIO
assert numeros_al_final_sorted([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]  # noqa: E501
# NO MODIFICAR - FIN
