"""For, Sum, Reduce."""


def sumatoria_basico(n: int) -> int:
    if n > 1:
        return sumatoria_basico(n-1) + sumatoria_basico(n-2)
    return n
for i in range(10):
    print(sumatoria_basico(i))

# NO MODIFICAR - INICIO
assert sumatoria_basico(1) == 1
assert sumatoria_basico(100) == 5050
# NO MODIFICAR - FIN


###############################################################################

def sumatoria_sum(n: int) -> int:
    """Re-Escribir utilizando la función sum.
    Restricción: No utilizar bucles (FOR, WHILE, etc)
    Referencia: https://docs.python.org/3/library/functions.html#sum
    """


# NO MODIFICAR - INICIO
assert sumatoria_sum(1) == 1
assert sumatoria_sum(100) == 5050
# NO MODIFICAR - FIN


###############################################################################


from typing import Iterable  # noqa: E402


def multiplicar_basico(numeros: Iterable[float]) -> float:
    """Toma un lista de números y devuelve el producto todos los númereos. Si
    la lista está vacia debe devolver 0.
    Restricciones:
        - No usar bibliotecas auxiliares (Numpy, math, pandas).
        - Utilizar un bucle FOR
        - Utilizar múltiples Return
        - No utilizar ELSE
    """


# NO MODIFICAR - INICIO
assert multiplicar_basico([1, 2, 3, 4]) == 24
assert multiplicar_basico([2, 5]) == 10
assert multiplicar_basico([]) == 0
assert multiplicar_basico([1, 2, 3, 0, 4, 5]) == 0
# NO MODIFICAR - FIN