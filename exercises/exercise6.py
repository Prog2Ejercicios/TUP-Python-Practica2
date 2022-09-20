"""Type, Comprensión de Listas, Sorted y Filter."""

from cgitb import text
from typing import List, Union


def numeros_al_final_basico(lista: List[Union[float, str]]) -> List[Union[float, str]]:  # noqa: E501
    """Toma una lista de enteros y strings y devuelve una lista con todos los
    elementos numéricos al final.

    Restricciones:
        - Utilizar un bucle FOR.
        - Utilizar la función type.
        - No utilizar índices.
    """
    lista_t=[]
    lista_n=[]
    for x in lista:
        if type(x) is int:
            lista_n.append(x)
            #agrega un elemento a lista_n si n un elemento de la lista es un extero
        else:
            #agrega un elemento a lista_t si n un elemento de la lista es un carácter
            lista_t.append(x)
    #finalmente agrega a lista_t los elementos de lista_n        
    lista_t.extend(lista_n)
    #retorna la lista_t
    return lista_t

# NO MODIFICAR - INICIO
assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]  # noqa: E501
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_comprension(lista: List[Union[float, str]]) -> List[Union[float, str]]:  # noqa: E501
    """Re-escribir utilizando comprensión de listas.

    Restricciones:
        - No utilizar bucles.
        - Utilizar dos comprensiones de listas.
    """
    n = [i for i in lista if type(i) is int]
    
    s = [i for i in lista if type(i) is str]
    
   
    return  s+n


# NO MODIFICAR - INICIO
assert numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]  # noqa: E501
# NO MODIFICAR - FIN
