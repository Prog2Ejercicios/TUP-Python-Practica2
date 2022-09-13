"""Type, Comprensión de Listas, Sorted y Filter."""

from typing import List, Union


def numeros_al_final_basico(lista: List[Union[float, str]]) -> List[Union[float, str]]:  # noqa: E501
    """Toma una lista de enteros y strings y devuelve una lista con todos los
    elementos numéricos al final.

    Restricciones:
        - Utilizar un bucle FOR.
        - Utilizar la función type.
        - No utilizar índices.
    """


# NO MODIFICAR - INICIO
    liststr=[]
    listint=[]
    for i in lista:
        if type(i) == int:
            listint.append(i)
        else:
            liststr.append(i)
    listastrint = liststr + listint
    return listastrint
assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]  # noqa: E501
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_comprension(lista: List[Union[float, str]]) -> List[Union[float, str]]:  # noqa: E501
    """Re-escribir utilizando comprensión de listas.

    Restricciones:
        - No utilizar bucles.
        - Utilizar dos comprensiones de listas.
    """


# NO MODIFICAR - INICIO
    listaLetras = []
    listaNros = []
    listaLetras = [var for var in lista if type(var) == str] 
    listaNros = [var for var in lista if type(var) == int]          #preguntar 
    lista = listaLetras + listaNros
    return lista
assert numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]) == (["a", "b", "j", 3, 1, 10])  # noqa: E501
# NO MODIFICAR - FIN
