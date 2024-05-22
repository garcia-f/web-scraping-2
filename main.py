import os
import requests
from bs4 import BeautifulSoup

#Funcion para crear un directorio si no existe
def directorio(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

#Funcion para descargar la imagen
def descargar(url, directory):
    #intenta descargar la imagen y si no puede imprime un mensaje de error
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(directory, 'wb') as f:
                f.write(response.content)
                print(f"imagen descargada: {url}")
        else:
            print(f"no se pudo descargar: {url}")
    except requests.exceptions.RequestException as e:
        print(f"hubo un error al descargar {url}: {e}")

#Funcion para obtener los datos de la url
def get_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    imagen = soup.find_all('img', src=True) #busca todas las imagenes de la pagina
    imagen_formatos = ['png', 'jpg', 'webp'] #formatos de imagenes validos
    directorio('imagenes') #crea el directorio imagenes
    for imagen in imagen: #recorre todas las imagenes
        imagen_url = imagen['src']
        if imagen_url.startswith(('http://', 'https://')): #verifica que el link sea valido
            imagen_extension = imagen_url.split('.')[-1].lower() #obtiene la extension de la imagen
            if imagen_extension in imagen_formatos: #verifica que la extension sea valida
                imagen_path = os.path.join('imagenes', os.path.basename(imagen_url)) 
                descargar(imagen_url, imagen_path)
            #si la extension no es valida imprime un mensaje
            else:
                print(f"no se descargo la imagen: {imagen_url} , el formato no es valido")
        else:
            print(f"no se descargo la imagen: {imagen_url} el link no es valido")

# url elegida
url = 'https://www.mercadolibre.com.ar/c/computacion#menu=categories'
get_data(url)