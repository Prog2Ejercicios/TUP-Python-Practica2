def maximo_basico(a: float, b: float) -> float:
    """Toma dos números y devuelve el mayor."""
    

print("Ingrese el primer numero: ")
a = float(input())
print("Ingrese el segundo numero: ")
b = float(input())


if a > b:
    print("El numero",a,"es mayor que",b)
elif b > a:
    print("El numero",b,"es mayo que",a)
else:
    print("Ambos numeros son iguales")



# NO MODIFICAR - INICIO
from exersice1 import maximo_basico


assert maximo_basico(10, 5) == 10
assert maximo_basico(9, 18) == 18
# NO MODIFICAR - FIN


###############################################################################


#def maximo_libreria(a: float, b: float) -> float:
"""Re-escribir utilizando el built-in max.
Referencia: https://docs.python.org/3/library/functions.html#max
"""


print("Ingrese el primer numero: ")
a = float(input())
print("Ingrese el segundo numero:")
b = float(input())

maximo_libreria = [a,b]

maximo_basico = max(maximo_libreria)


print("El numero mayo es: ", maximo_libreria)



###############################################################################


def maximo_ternario(a: float, b: float) -> float:
    """Re-escribir utilizando el operador ternario.
    Referencia: https://docs.python.org/3/reference/expressions.html#conditional-expressions # noqa: E501
    """

print("Ingrese el primer número: ")
a = float(input())
print("Ingrese el segundo número: ")
b = float(input())

numeros = [a,b]

maximo_ternario = max(numeros)


# NO MODIFICAR - INICIO
assert maximo_ternario(10, 5) == 10
assert maximo_ternario(9, 18) == 18
# NO MODIFICAR - FIN
