from funciones import *
from PIL import Image
import numpy as np
import os

def main(): 
    img = imagen()
    metodo = metodo_usar()
    if metodo.lower() == "pixel":
        tam_bloque,niveles_color = tamaños_metodo(metodo) # nos devuelve el tamaño del bloque y la cantidad de niveles de color
        imagen_final = pixel(img,tam_bloque,niveles_color) # nos devuelve la imagen con los pixeles cambiados
        ruta_salida = imagen_final_output(imagen_final) # nos devuelve la ruta de salida de la imagen
        print(ruta_salida)
    elif metodo.lower() == "ascii":
        ancho = tamaños_metodo(metodo) # nos devuelve el ancho de la imagen
        imagen_final = ascii(img,ancho) # nos devuelve la imagen ascii
        print(imagen_final)
    
              

if __name__ == "__main__":
    main()
