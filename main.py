from PIL import Image
import numpy as np

def imagen()->Image:
    img = input("Ingrese la ruta de la imagen: ")
    try:
        img = Image.open(img)
    except FileNotFoundError:
        print("no hay imagen para esa ruta")
        exit()
    return img

def metodo_usar()->str:
    metodo = input("Ingrese el metodo a usar(Pixel/Ascii): ")
    return metodo

def tamaño(metodo:str)-> tuple[int,int] | int:
    if metodo.lower() == "pixel":
        tam_bloque = input("Ingrese el tamaño del bloque: ")
        niveles_color = input("Ingrese el número de niveles de color: ")
        if len(tam_bloque) == 0 or int(tam_bloque) <= 0 :
            tam_bloque = 10 
        if len(niveles_color) == 0 or int(niveles_color) <= 0:
            niveles_color = 4
        return int(tam_bloque),int(niveles_color)
        
    elif metodo.lower() == "ascii":
        ancho_imagen = input("Ingrese el ancho de la imagen: ")
        if len(ancho_imagen) == 0 or int(ancho_imagen) <= 0 :
           ancho_imagen= 100
        return int(ancho_imagen)
    
def pixel(img:Image, tam_bloque:int, niveles_color:int):
    array_pixeles = np.array(img)
    alto, ancho = array_pixeles.shape[0],array_pixeles.shape[1]
    colores_posibles = np.linspace(0,255,niveles_color).astype(int)
    for altura in range(0,alto, tam_bloque):
        for anchura in range(0,ancho, tam_bloque):

   
    
def main():
    img = imagen()
    metodo = metodo_usar()
    if metodo.lower() == "pixel":
        tam_bloque,niveles_color = tamaño(metodo)
        pixel(img,tam_bloque,niveles_color)

if __name__ == "__main__":
    main()


    
