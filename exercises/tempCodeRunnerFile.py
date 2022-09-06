
# numeros_al_cubo = map(lambda x: x ** 3, numeros) # Completar


# """
# Escribir una función lambda que permita filtrar todos los elementos pares

# Restricción: Utilizar List, filter, lambda y la variable numeros_al_cubo
# """

# numeros_al_cubo_pares = filter(lambda x: not (x%2) != 0, numeros_al_cubo) # Completar


# """
# Escribir una función Lambda que sume todos los elementos

# Restricción: Utilizar reduce, lambda y la variable numeros_al_cubo_pares
# """

# from functools import reduce  # noqa: E402

# suma_numeros_al_cubo_pares = reduce(lambda x,y: x + y, numeros_al_cubo_pares) # Completar


# # NO MODIFICAR - INICIO
# assert numeros_al_cubo == [1, 8, 27, 64, 125, 216]
# assert numeros_al_cubo_pares == [8, 64, 216]
# assert suma_numeros_al_cubo_pares == 288
# # NO MODIFICAR - FIN
