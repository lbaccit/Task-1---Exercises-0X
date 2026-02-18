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

def infimum(imagen1: bytes, imagen2: bytes) -> bytes:
    return bytes(min(p1, p2) for p1, p2 in zip(imagen1, imagen2))

def main():
    if len(sys.argv) != 4:
        print("Uso: python exercise_02c_inf.py imagen1.pgm imagen2.pgm resultado.pgm")
        sys.exit(2)
    path1, path2, output_path = sys.argv[1], sys.argv[2], sys.argv[3]
    ancho1, alto1, max_valor1, imagen1, header1 = leer_imagen(path1)
    ancho2, alto2, max_valor2, imagen2, header2 = leer_imagen(path2)
    if (ancho1, alto1) != (ancho2, alto2):
        raise ValueError("Las imágenes deben tener las mismas dimensiones.")
    output_pixels = infimum(imagen1, imagen2)
    escribir_pgm(output_path, header1, output_pixels)

if __name__ == "__main__":
    try:
        main()
    except Exception:
        traceback.print_exc()
