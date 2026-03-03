import sys
def exercise_02b_compare(path1: str, path2: str):
    with open(path1, "rb") as imagen1:
        tipo1 = imagen1.readline()
        dimensiones1= imagen1.readline()
        while dimensiones1.startswith(b"#"):
            dimensiones1 = imagen1.readline()
        maximo1 = imagen1.readline()
        while maximo1.startswith(b"#"):
            maximo1 = imagen1.readline()
        partes1 = dimensiones1.split()
        ancho1 = int(partes1[0])
        alto1 = int(partes1[1])
        pixels1 = imagen1.read()

    with open(path2, "rb") as imagen2:
        tipo2 = imagen2.readline()
        dimensiones2= imagen2.readline()
        while dimensiones2.startswith(b"#"):
            dimensiones2 = imagen2.readline()
        maximo2 = imagen2.readline()
        while maximo2.startswith(b"#"):
            maximo2 = imagen2.readline()
        partes2 = dimensiones2.split()
        ancho2 = int(partes2[0])
        alto2 = int(partes2[1])
        pixels2 = imagen2.read()   
    iguales = True
    if ancho1 != ancho2 or alto1 != alto2:
        iguales = False
    if iguales:
        if pixels1 != pixels2:
            iguales = False
    with open("exercise_02b_output_01.txt", "w") as f:
            if iguales:
                f.write("1")
            else:
                f.write("0")  

#exercise_02b_compare("cam_74.pgm", "cam_74.pgm" )

if __name__ == "__main__":
    input_path = sys.argv[1]
    output_path = sys.argv[2]

    exercise_02b_compare(input_path, output_path)