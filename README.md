# Task-1---Exercises-0X

Rocio Marquez -  rocio.marquez@alumnos.upm.es

Luciana Bacci T - l.bacci@alumnos.upm.es

Las carpetas contienen los códigos ejecutables, la persona que los ejecute debera colocar los respectivos inputs en la consola, ejemplo del ejercicio 2
ejecutar: ""python exercise_02a_thresh.py cam_74.pgm 100 cam_74_100_output.pgm"", teniendo en cuenta que el archivo del primer argumento debe ser un archivo existente en el mismo directorio del código o con una ruta al archivo designado, en el caso del output es la salida esperada, por lo que el nombre que se le asigna, sera el archivo de salida.

En ciertos codigos hay lineas comentadas por si es requerido observar el output de saluda en forma de imagen con la libreria iio, si no es necesario, se puede comentar la importación de esa librería si es que no es necesario y se dificulta la ejecución.

Ejercicio 02c:

Para ejecutar el codigo, se debe ubicar en la carpeta de exercise_02c en la terminal. El codigo recibe 2 imagenes en formato .pgm (ambas con las mismas dimensiones) y se genera una imagen en formato .pgm. Para calcular el supremum entre las dos imagenes, toca ejecutar lo siguiente: 
python3 exercise_02c_sup.py image1.pgm image2.pgm out_sup.pgm
Y para calcular el infimum, se ejecuta lo siguiente: 
python3 exercise_02c_inf.py image1.pgm image2.pgm out_inf.pgm

Ejercicio 3ab:

Para ejecutar el código, se debe ubicar en la carpeta de exercise_03 en la terminal. El código recibe 1 imagen en formato .pgm, un valor size que indica el tamaño de la operación morfológica, y genera una imagen de salida en formato .pgm. Para calcular la erosión de la imagen, toca ejecutar lo siguiente:
python3 exercise_03a_erosion.py immed_gray_inv.pgm 1 out_ero1.pgm
Y para calcular la dilatación, se ejecuta lo siguiente:
python3 exercise_03b_dilation.py immed_gray_inv.pgm 1 out_dil1.pgm

Si se desea aplicar la operación con un tamaño mayor, simplemente se cambia el valor de size; por ejemplo, usando 2 se obtiene una erosión o dilatación equivalente a aplicar la operación elemental dos veces consecutivas

