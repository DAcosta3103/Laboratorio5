#Laboratorio5 Diego José Acosta Obando C00041

# ---------------------------------- Bibliotecas ------------------------------

#Esta biblioteca es para que el programa pueda leer y actuar con lo que se escripa en la línea de comandos
import argparse 
#Acá importamos las bibliotecas necesarias para el procesamiento de imagenes (OpenCV y PIL)
import cv2
from PIL import Image

# ---------------------------------- Funciones ------------------------------

# Acá creamos la interfaz común para mostrar imágenes
class MostrarImagen:
	def mostrar_imagen(self, ruta_imagen):
		raise NotImplementedError("Método no implementado")

#Acá programamos el uso de la biblioteca PIL
class PILMostrarImagen(MostrarImagen):
	def mostrar_imagen(self, ruta_imagen):
		imagen = Image.open(ruta_imagen)
		imagen.show()

#Acá programamos el uso de la biblioteca OpenCV
class OpenCVMostrarImagen(MostrarImagen):
	def mostrar_imagen(self, ruta_imagen):
		imagen = cv2.imread(ruta_imagen)
		cv2.imshow("Imagen", imagen)
		cv2.waitKey(0)
		cv2.destroyAllWindows()


#Acá creamos una función para analizar argumentos de la línea de comandos
def parse_args():
    parser = argparse.ArgumentParser(description="Procesamiento de Imágenes")
    parser.add_argument("--biblioteca", choices=["PIL", "OpenCV"], required=True, help="Biblioteca para procesamiento de imágenes")
    parser.add_argument("--imagen", required=True, help="Ruta de la imagen a procesar")
    return parser.parse_args()

# ---------------------------------- Main ------------------------------
def main():
	args = parse_args()

#Acá se le pide al usuario seleccionar una biblioteca
	if args.biblioteca == 'PIL':
		visor = PILMostrarImagen()
	elif args.biblioteca == 'OpenCV':
		visor = OpenCVMostrarImagen()
	else:
		print("Ups! Biblioteca no válida. Por favor seleccione la biblioteca 'PIL' u 'OpenCV'.")
	return

#Acá se muestra la imagen, en el caso en que se introduzca una biblioteca correcta y una imágen válida
	try:
		visor.mostrar_imagen(args.imagen)
	except Exception as e:
		print(f"Ups! Ha ocurrido un error al procesar la imagen: {e}")

#Finalmente tenemos el punto de entrada del programa
if __name__ == "__main__":
    main()

