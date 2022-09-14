"""Bloque IF, operadores lógicos, función max y operador ternario."""


from calendar import c


def maximo_basico(a: float, b: float) -> float:
    if a > b:
        maximo_basico = a
        return maximo_basico
    if a < b:
        maximo_basico = b
        return maximo_basico
    

    """Toma dos números y devuelve el mayor.
    Restricciones:
        - Utilizar IF
        - No utilizar ELSE
        - No utilizar la función max
"""


# NO MODIFICAR - INICIO
assert maximo_basico(10, 5) == 10
assert maximo_basico(9, 18) == 18
# NO MODIFICAR - FIN


###############################################################################


def maximo_libreria(a: float, b: float) -> float:
    return max(a,b)
    
    """Re-escribir utilizando el built-in max.
    Referencia: https://docs.python.org/3/library/functions.html#max
    """
    

# NO MODIFICAR - INICIO
assert maximo_libreria(10, 5) == 10
assert maximo_libreria(9, 18) == 18
# NO MODIFICAR - FIN


###############################################################################


def maximo_ternario(a: float, b: float) -> float:
    maximo_ternario = a if a > b else b
    return maximo_ternario
    """Re-escribir utilizando el operador ternario.
    Referencia: https://docs.python.org/3/reference/expressions.html#conditional-expressions # noqa: E501
    """


# NO MODIFICAR - INICIO
assert maximo_ternario(10, 5) == 10
assert maximo_ternario(9, 18) == 18
# NO MODIFICAR - FIN