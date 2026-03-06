import sys
import traceback
# imageio.v3 as iio

def limpiar_informacion(datos: bytes, i:int) -> int:
    n = len(datos)
    while i < n:
        linea = datos[i]
        #Saltar espacios en blanco
        if linea in b"\t\r\n ":
            i += 1
            continue
        #Saltar comentarios
        if linea == ord("#"):
            while i < n and datos[i] not in (10, 13):
                i += 1
            continue
        break
    return i

def obtener_informacion(datos: bytes, i:int):
    info = limpiar_informacion(datos, i)
    if info >= len(datos):
        raise ValueError("No se encontró información después de limpiar los datos.")
    inicio = info
    while info < len(datos) and datos[info] not in b"\t\r\n# ":
        info += 1
    token = datos[inicio:info].decode("ascii")
    return token, info

def leer_imagen(path:str):
    data = open(path, "rb").read()
    i = 0
    formato, i = obtener_informacion(data, i)
    if formato not in ("P5", "P2"):
        raise ValueError("Formato no soportado: {}".format(formato))
    ancho, i = obtener_informacion(data, i)
    ancho = int(ancho)
    alto, i = obtener_informacion(data, i)
    alto = int(alto)
    max_valor, i = obtener_informacion(data, i)
    max_valor = int(max_valor)
    if max_valor > 255:
        raise ValueError("Valor máximo no soportado: {}".format(max_valor))
    if ancho <= 0 or alto <= 0:
        raise ValueError("Dimensiones no válidas: {}x{}".format(ancho, alto))
    
    i = limpiar_informacion(data, i)
    pixeles = ancho * alto

    if formato == "P5":
        if i + pixeles > len(data):
            raise ValueError("Datos de píxeles insuficientes para la imagen.")
        imagen = data[i:i+pixeles]
    else:
        #Leer P2
        valores = []
        index = i
        for _ in range(pixeles):
            t, index = obtener_informacion(data, index)
            valor = int(t)
            if not (0 <= valor <= max_valor):
                raise ValueError("Valor de píxel fuera de rango: {}".format(valor))
            valores.append(valor)
        imagen = bytes(valores)

    output = f"{formato}\n{ancho} {alto}\n{max_valor}\n".encode("ascii")
    return ancho, alto, max_valor, imagen, output

def escribir_pgm(path:str, header: bytes, pixeles: bytes):
    with open(path, "wb") as f:
        f.write(header)
        f.write(pixeles)

def bytes_matriz(imagen:bytes, ancho:int, alto:int):
    matriz = []
    for i in range(alto):
        fila = []
        for j in range(ancho):
            fila.append(imagen[i*ancho + j])
        matriz.append(fila)
    return matriz

def matriz_bytes(matriz) -> bytes:
    pixeles = []
    for fila in matriz:
        for valor in fila:
            pixeles.append(valor)
    return bytes(pixeles)


def calculos(matriz, ancho:int, alto:int):
    resultado = [[0 for i in range(ancho)] for j in range(alto)]

    for i in range(alto):
        for j in range(ancho):
            maximo = 0
            for y in (-1, 0, 1):
                for x in (-1, 0, 1):
                    ny = i + y
                    nx = j + x
                    if 0 <= ny < alto and 0 <= nx < ancho:
                        if matriz[ny][nx] > maximo:
                            maximo = matriz[ny][nx]
            resultado[i][j] = maximo
    return resultado

def dilatacion(imagen:bytes, ancho:int, alto:int, size:int) -> bytes:
    if size < 1:
        raise ValueError("El tamaño de la dilatación debe ser  mayor  o igual 1")
    
    matriz = bytes_matriz(imagen, ancho, alto)

    for _ in range(size):
        matriz = calculos(matriz, ancho, alto)
    return matriz_bytes(matriz)

def main():
    if len(sys.argv) != 4:
        print("Uso: python exercise_03a.py imagen.pgm size resultado.pgm")
        sys.exit(2)
    
    path, size, resultado_path = sys.argv[1], sys.argv[2], sys.argv[3]
    size = int(size)

    ancho, alto, max_valor, imagen, header = leer_imagen(path)
    output_pixeles = dilatacion(imagen, ancho, alto, size)
    escribir_pgm(resultado_path, header, output_pixeles)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error:", e)
        traceback.print_exc()

