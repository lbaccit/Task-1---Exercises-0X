import matplotlib.pyplot as plt
import imageio.v3 as iio 
import sys
def exercise_02a_thresh(input_path: str, threshold_value: int, output_path: str):
    with open(input_path, "rb") as imagen:
        tipo = imagen.readline()  #P2 o P5
        dimensiones = imagen.readline()
        while dimensiones.startswith(b"#"):
            dimensiones = imagen.readline()

        
        maximo = imagen.readline()
        while maximo.startswith(b"#"):
            maximo = imagen.readline()

        #convertimos dimensiones a numeros normales (antes eran binarios)
        partes = dimensiones.split()
        ancho = int(partes[0])
        alto = int(partes[1])

        valor_maximo_gris = int(maximo)

        # Leemos todos los píxeles restantes como bytes
        pixeles = bytearray(imagen.read())
        # bytearray permite modificar cada pixel

        nuevos_pixeles = bytearray(len(pixeles))

        for i in range(len(pixeles)):
            if pixeles[i] >= threshold_value:
                nuevos_pixeles[i] = 255
            else: 
                nuevos_pixeles[i] = 0

        with open(output_path, "wb") as f:
            f.write(tipo) #escribimos P5
            f.write(dimensiones) #ancho y alto
            f.write(str(valor_maximo_gris).encode() + b"\n") #maximo gris
            f.write(nuevos_pixeles) #pixeles modificafos
        





if __name__ == "__main__":
    input_path = sys.argv[1]
    i = int(sys.argv[2])
    output_path = sys.argv[3]

    exercise_02a_thresh(input_path, i, output_path)
    #img = iio.imread("salida.pgm") #si se quiere visualizar descomentar img y colocar en output_path salida.pgm
    #img = iio.imread("cam_74_100_output.pgm")

# mostrar imagen
    #plt.imshow(img, cmap="gray")  
    #plt.title("Imagen_salida PGM")
    #plt.axis("off")  
    #plt.show()
    






        

