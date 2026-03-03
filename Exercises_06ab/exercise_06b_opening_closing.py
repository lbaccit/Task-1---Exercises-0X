import sys
import matplotlib.pyplot as plt
import imageio.v3 as iio 
def erosion(pixels, ancho, alto, i):
    #resultado = bytearray(len(pixels))
    resultado = bytearray(len(pixels))
    for y in range(alto):
        for x in range(ancho):
            todos_blancos = True
          #vamos a recorrer dy y dx dependiendo de i y el cuadrado viendo si son todos blancos o negro
            minimo = 255
            for dy in range(-i, i +1):
                for dx in range(-i, i +1):
                    nx = x + dx
                    ny = y + dy

                    if nx <0 or ny <0 or nx>= ancho or ny>= alto:
                        #todos_blancos = False # nos acotamos al cuadrado
                        continue
                    indice = ny * ancho + nx
                    #valor = 255 if nx<0 or ny<0 or nx>=ancho or ny>=alto else pixels[ny*ancho + nx]
                    valor = pixels[ny * ancho + nx]
                    #valor = pixels[indice]
                    if valor<minimo:
                        minimo = valor
                    #if pixels[indice] == 0:
                        #todos_blancos = False
            indice_actual = y * ancho + x
            resultado[indice_actual] = minimo
            #resultado[indice_actual] = minimo
            #if todos_blancos:
                #resultado[indice_actual] = 255
            #else:
                #resultado[indice_actual] = 0
    return resultado

def dilatacion(pixels, ancho, alto, i):
    resultado = bytearray(len(pixels))

    for y in range(alto):
        for x in range(ancho):
            maximo = 0
            #algun_blanco = False
            for dy in range(-i, i +1):
                for dx in range(-i, i +1 ):
                    
                    nx = x +dx
                    ny = y + dy

                    if nx <0 or ny <0 or nx>=ancho or ny>=alto:
                        continue
                    indice = ny * ancho + nx
                    valor = pixels[indice]
                    #valor = 0 if nx<0 or ny<0 or nx>=ancho or ny>=alto else pixels[ny*ancho + nx]
                    #valor = pixels[ny * ancho + nx]

                    if valor > maximo:
                        maximo = valor
                    

                    #if pixels[indice] == 255:
                        #algun_blanco = True
            indice_actual = y * ancho +x
            resultado[indice_actual] = maximo
            #if algun_blanco:
                #resultado[indice_actual] = 255
            #else:
                #resultado[indice_actual] = 0
    return resultado

def exercise_06a_closing_opening(i, input_path, output_path):
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
#opening

    dilatada = dilatacion(pixels, ancho, alto, i)
    resultado = erosion(dilatada, ancho, alto, i)

    erosionada = erosion(resultado, ancho, alto, i)
    abierta = dilatacion(erosionada, ancho, alto, i)


#closing
    with open(output_path, "wb") as f:
        f.write(tipo)
        f.write(dimensiones)
        f.write(maximo)
        f.write(abierta)

if __name__ == "__main__":

    i = int(sys.argv[1])
    input_path = sys.argv[2]
    output_path = sys.argv[3]

    exercise_06a_closing_opening(i, input_path, output_path)
    #img = iio.imread("salida.pgm")
    #img2 = iio.imread("immed_gray_inv_20051123_ope2clo2.pgm")

# Mostrar imagen
    #plt.imshow(img, cmap="gray")  
    #plt.title("Imagen_salida PGM")
    #plt.axis("off")  
    #plt.show()
    