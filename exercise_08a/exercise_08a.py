import sys

def erosion(pixels, ancho, alto, i):

    resultado = bytearray(len(pixels))

    for y in range(alto):
        for x in range(ancho):

            minimo = 255

            for dy in range(-i, i+1):
                for dx in range(-i, i+1):

                    nx = x + dx
                    ny = y + dy

                    if nx < 0 or ny < 0 or nx >= ancho or ny >= alto:
                        continue

                    indice = ny * ancho + nx
                    valor = pixels[indice]

                    if valor < minimo:
                        minimo = valor

            indice_actual = y * ancho + x
            resultado[indice_actual] = minimo

    return resultado


def dilatacion(pixels, ancho, alto, i):

    resultado = bytearray(len(pixels))

    for y in range(alto):
        for x in range(ancho):

            maximo = 0

            for dy in range(-i, i+1):
                for dx in range(-i, i+1):

                    nx = x + dx
                    ny = y + dy

                    if nx < 0 or ny < 0 or nx >= ancho or ny >= alto:
                        continue

                    indice = ny * ancho + nx
                    valor = pixels[indice]

                    if valor > maximo:
                        maximo = valor

            indice_actual = y * ancho + x
            resultado[indice_actual] = maximo

    return resultado


def opening(pixels, ancho, alto, i):

    er = erosion(pixels, ancho, alto, i)
    return dilatacion(er, ancho, alto, i)


def closing(pixels, ancho, alto, i):

    di = dilatacion(pixels, ancho, alto, i)
    return erosion(di, ancho, alto, i)

#vamos a medir el ruido de cada uno 
def medir_ruido(img, ancho, alto):

    ruido = 0

    for y in range(1, alto-1):
        for x in range(1, ancho-1):

            centro = img[y*ancho + x]

            suma = 0
            n = 0

            for dy in range(-1,2):
                for dx in range(-1,2):

                    if dx == 0 and dy == 0:
                        continue

                    nx = x + dx
                    ny = y + dy

                    suma += img[ny*ancho + nx]
                    n += 1

            promedio = suma / n

            if abs(centro - promedio) > 100:
                ruido += 1

    return ruido

def exercise_08a(input_path):

    with open(input_path, "rb") as f:

        tipo = f.readline()

        dimensiones = f.readline()
        while dimensiones.startswith(b"#"):
            dimensiones = f.readline()

        maximo = f.readline()
        while maximo.startswith(b"#"):
            maximo = f.readline()

        partes = dimensiones.split()
        ancho = int(partes[0])
        alto = int(partes[1])

        pixels = bytearray(f.read())

    i = 1  

    # filtros

    F1 = opening(pixels, ancho, alto, i)
    F2 = closing(pixels, ancho, alto, i)
    F3 = closing(opening(pixels, ancho, alto, i), ancho, alto, i)
    F4 = opening(closing(pixels, ancho, alto, i), ancho, alto, i)


    r1 = medir_ruido(F1, ancho, alto)
    r2 = medir_ruido(F2, ancho, alto)
    r3 = medir_ruido(F3, ancho, alto)
    r4 = medir_ruido(F4, ancho, alto)

    resultados = [(1,r1),(2,r2),(3,r3),(4,r4)]
#ordenamos los mejores
    resultados.sort(key=lambda x: x[1])

    mejor1 = resultados[0][0]
    mejor2 = resultados[1][0]
#elegimos los mejores y los añadimos al texto
    with open("exercise_08a_output_01.txt","w") as f:

        f.write(str(mejor1) + "\n")
        f.write(str(mejor2))


if __name__ == "__main__":

    input_path = sys.argv[1]

    exercise_08a(input_path)