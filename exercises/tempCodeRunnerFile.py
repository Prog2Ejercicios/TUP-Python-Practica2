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
    lista1=[]
    lista2=[]
    for i in lista:
        if type(lista)==str:
            lista1.append(i)
        else:
            lista2.append(i)
    lista1.extend(lista2)
    print(lista1)


assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]