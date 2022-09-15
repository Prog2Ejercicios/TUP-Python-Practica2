"""Sum, Compresión de Listas, Map, Filter, Reduce."""

from typing import Iterable


def suma_cubo_pares_for(numeros: Iterable[int]) -> int:
    """Toma una lista de números, los eleva al cubo, y devuelve la suma de
    los elementos pares.

    Restricciones:
        - Utilizar dos bucles FOR.
        - No utilizar la función range.

    Referencias:
        - https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions # noqa: E501
        - https://docs.python.org/3/library/functions.html#sum
    """


# NO MODIFICAR - INICIO
    cubo=[]
    suma=[]
    for i in numeros:
        cubo.append(i**3)
    for i in cubo:
        if i % 2 == 0:
            suma.append(i)
    res=(sum(suma)) 
    return res      

assert suma_cubo_pares_for([1, 2, 3, 4, 5, 6]) == 288
# NO MODIFICAR - FIN