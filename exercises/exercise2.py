"""Comparaciones Encadenadas, Cantidad Arbitraria de Parámetros, Recursividad.
"""


def maximo_encadenado(a: float, b: float, c: float) -> float:
    
    if a<b>c:
        return b
    if b<a>c:
        return a
    return c


# NO MODIFICAR - INICIO
assert maximo_encadenado(1, 10, 5) == 10
assert maximo_encadenado(5, 10, 1) == 10
assert maximo_encadenado(5, 10, 5) == 10

assert maximo_encadenado(4, 9, 18) == 18
assert maximo_encadenado(9, 4, 18) == 18
assert maximo_encadenado(9, 9, 18) == 18

assert maximo_encadenado(24, 9, 18) == 24
assert maximo_encadenado(24, 18, 9) == 24
assert maximo_encadenado(24, 18, 18) == 24
# NO MODIFICAR - FIN


###############################################################################


def maximo_cuadruple(a: float, b: float, c: float, d: float) -> float:
   return max(a,b,c,d)


# NO MODIFICAR - INICIO
assert maximo_cuadruple(1, 10, 5, -5) == 10
assert maximo_cuadruple(4, 9, 18, 6) == 18
assert maximo_cuadruple(24, 9, 18, 20) == 24
assert maximo_cuadruple(24, 9, 18, 30) == 30
# NO MODIFICAR - FIN


###############################################################################


def maximo_arbitrario(*args) -> float:
   return max(args)

# NO MODIFICAR - INICIO
assert maximo_arbitrario(1, 10, 5, -5) == 10
assert maximo_arbitrario(4, 9, 18, 6) == 18
assert maximo_arbitrario(24, 9, 18, 20) == 24
assert maximo_arbitrario(24, 9, 18, 30) == 30
# NO MODIFICAR - FIN
