import sys

def limpiar_informacion(datos: bytes, i:int) -> int:
    n = len(datos)
    while i < n:
        linea = datos[i]
        if linea in b"\t\r\n ":
            i += 1
            continue
        if linea == ord(b"#"):
            while i < n and datos[i] not in ord(b"\n"):
                i += 1
            continue
        break
    return i
