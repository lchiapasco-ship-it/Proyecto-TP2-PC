from PIL import Image
import numpy as np

def imagen()->Image:
    while True:
        ruta_img = input("Ingrese la ruta de la imagen: ")     #Pedimos la ruta de la imagen sobre la que uqiere interactuar
        try:
            return Image.open(ruta_img)  # probamos abrir la imagen
        except Exception as e: # si hay algun error
            print(f"El error es {e}") # lo mostramos al usuario


def metodo_usar()->str:
    metodo = input("Ingrese el metodo a usar(Pixel/Ascii): ")
    while metodo.lower() != "pixel" and metodo.lower() != "ascii":  # nos fijamos si el usaurio escribio pixel o ascii sin importar si con mayusculas o minusculas por que los convertimos a minusculas
        print("Metodo no valido")
        metodo = input("Ingrese el metodo a usar(Pixel/Ascii): ")
        
    return metodo

def tamaño(metodo:str)-> tuple[int,int] | int:
    if metodo.lower() == "pixel":
        tam_bloque = input("Ingrese el tamaño del bloque: ")
        niveles_color = input("Ingrese el número de niveles de color: ")
        if len(tam_bloque) == 0 or int(tam_bloque) <= 0 or not tam_bloque.isdigit():  # si no ingresa nada o el numero es menor o igual a 0 o no es una cadena de digitos se le asigna 10
            tam_bloque = 10 
        if len(niveles_color) == 0 or int(niveles_color) <= 0 or not niveles_color.isdigit():  # si no ingresa nada o el numero es menor o igual a 0 o no es una cadena de digitos se le asigna 4
            niveles_color = 4
        return int(tam_bloque),int(niveles_color)
        
    elif metodo.lower() == "ascii":
        ancho_imagen = input("Ingrese el ancho de la imagen: ")
        if len(ancho_imagen) == 0 or int(ancho_imagen) <= 0 or not ancho_imagen.isdigit():  # si no ingresa nada o el numero es menor o igual a 0  o no es una cadena de digitos se le asigna 100 
           ancho_imagen= 100
        return int(ancho_imagen)
    
def pixel(img:Image, tam_bloque:int, niveles_color:int)->Image:
    array_pixeles = np.array(img) # creamos el array de pixeles en base a la imagen que va a tener 3 valores [r,g,b]
    alto, ancho = array_pixeles.shape[0],array_pixeles.shape[1] # sacamos la altura y anchura de la imgan
    colores_posibles = np.linspace(0,255,niveles_color).astype(int) # sacamos los valores posibles (entre 0 y 255 , niveles de color = canitdad de nveles que hay entre el 0 y el 256)
    for fila in range(0,alto,tam_bloque): #Indicamos el tamaño del bloque 0(inicio), alto en filas(altura de imagen/fin) , tamaño de bloque como intervalo para separar en bloques en esos intervalos
        for columna in range(0,ancho,tam_bloque): #Indicamos el tamaño del bloque 0(inicio), ancho en columnas(altura de imagen/fin) , tamaño de bloque como intervalo para separar en bloques en esos intervalos
            pixel = array_pixeles[fila:tam_bloque+fila,columna:tam_bloque+columna] #Creamos los pixeles con los tamaños de fila y columnas de los bloques sacandolos del array ancho = fila:tam_bloque+fila y ancho = columna:tam_bloque+columna
            columna1_r = []
            columna2_g = []     # Creamos 3 listas para guardar los valores rgb de cada pixel en nuestro bloque
            columna3_b = []
            for fila_bloque in pixel: # iteramos en cada fila de nuestro floque entrando a cada pixel compueto por [r,g,b]
                for pixel_bloque in fila_bloque:
                    columna1_r.append(pixel_bloque[0]) #Guardamos su valor r , g y b en las listas
                    columna2_g.append(pixel_bloque[1])
                    columna3_b.append(pixel_bloque[2])
            media_columna_1_r = sum(columna1_r)/len(columna1_r)   #Hacemos la media de cada columna de cada bloque para sacar los valores rgb de cada bloque en total lo hacemos sumando cada columna y dividiendo por cadntidad de filas
            media_columna_2_g = sum(columna2_g)/len(columna2_g)
            media_columna_3_b = sum(columna3_b)/len(columna3_b)
            media_rgb = [media_columna_1_r,media_columna_2_g,media_columna_3_b] # Creamos una lista con los valores medios rgb de cada bloque
            color_r_final = {}
            color_g_final = {}      #Creamos diccionarios para guardar con key y value los valores y la resta entre el valor medio y el color posible
            color_b_final = {}
            for color in colores_posibles:
                color_r_final[color] = abs(media_rgb[0]-color)
                color_g_final[color] = abs(media_rgb[1]-color)      #Aplicamos abs para que queden todos numeros positivos enteros para que cuando saquemos el min en base a cada key nos de cual es el color mas cercano
                color_b_final[color] = abs(media_rgb[2]-color)         # nos quedan dicts asi {color posible(85): resta entre el valor medio y el color posible(125-85) } y asi con todos
            r_final = min(color_r_final , key=color_r_final.get)
            g_final = min(color_g_final , key=color_g_final.get)   # en base a los dicts usamos min para sacar el numero mas chico para cada key y el min hacemos .get para sacar ese valor y guardarlo como el promedio para valor de r
            b_final = min(color_b_final , key=color_b_final.get)
            for fila_pixel in range(fila, tam_bloque+fila):  # entramos en cada fila de nuestro bloque
                for columna_pixel in range(columna, tam_bloque+columna): # entramos en cada columna de nuestro bloque
                    array_pixeles[fila_pixel,columna_pixel, 0] = r_final  # le damos valor de color a cada pixel de nuestro bloque teniendo en cuenta que r = 0 , g = 1 y b = 2 en cada pixel
                    array_pixeles[fila_pixel,columna_pixel, 1] = g_final
                    array_pixeles[fila_pixel,columna_pixel, 2] = b_final                   
    formato_img = array_pixeles.astype(np.uint8) # convertimos el array en formato de imagen
    imagen_final = Image.fromarray(formato_img) #convertimos nuestro array en formato imagen en una imagen 
    return imagen_final # devolvemos imagen
            
 
            

def imagen_final_output(imagen_final:Image) -> str:
    while True:
        ruta_salida = input("Ingrese la ruta de salida de la imagen: ")   #Pedimos la ruta en la que se quiere guardar la imagen
        try:
            imagen_final.save(ruta_salida) # probamos guardar la imagen
            return "Proceso exitoso" # si se guarda devolvemos que funciono
        except Exception as e: # si hay algun error
            print(f"El error es {e}") # lo mostramos al usuario
        


    
def main():
    img = imagen()
    metodo = metodo_usar()
    if metodo.lower() == "pixel":
        tam_bloque,niveles_color = tamaño(metodo)
        imagen_final = pixel(img,tam_bloque,niveles_color)
        ruta_salida = imagen_final_output(imagen_final)
        print(ruta_salida)
        
    
              

if __name__ == "__main__":
    main()


    
