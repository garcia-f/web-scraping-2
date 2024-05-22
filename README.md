# Web Scraping and JSON Storage
Este tarea demuestra cómo realizar web scraping utilizando las bibliotecas Python requests y BeautifulSoup. El script obtiene imagenes del [URL](-https://www.mercadolibre.com.ar/c/computacion#menu=categories) de Mercado Libre, extrayendo del elemento <img> (png, jpg y webp.) y almacenando los resultados en una carpeta de imagenes.


- Instalar virtualenv si no está instalado
```bash
pip install virtualenv
```

- Crear un nuevo entorno virtual
```bash
virtualenv (nombre del entorno)
```

- Activar el entorno
```bash
(nombre del entorno)\Scripts\activate
```


- volver a la carpeta principal e instalar dependencias
```bash
pip install requests
```
```bash
pip install beautifulsoup4
```

## hacer correr el script
```bash
python main.py
```