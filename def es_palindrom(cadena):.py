def es_palindrom(cadena):
    """Retorna True si la cadena és un palíndrom, False en cas contrari."""
    # Eliminem espais i convertim a minúscules per a una comparació correcta
    cadena_neta = cadena.replace(" ", "").lower()
    # Comprovem si la cadena és igual a la seva inversa
    return cadena_neta == cadena_neta[::-1]

# Proves de la funció
print(es_palindrom("radar"))    # Retorna True
print(es_palindrom("ara"))      # Retorna True
print(es_palindrom("civic"))    # Retorna True
print(es_palindrom("rallar"))   # Retorna False
print(es_palindrom("tapat"))    # Retorna True
print(es_palindrom("simis"))    # Retorna True
print(es_palindrom("refer"))    # Retorna True
print(es_palindrom("Hola"))     # Retorna False