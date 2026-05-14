# Presentación técnica


## Título: Tests unitarios

### Descripción:

Este software consiste en una serie de tests unitarios realizados sobre un simple programa de
python que ordena una serie de palabras introducidas.

### Tecnologías utilizadas:

- Python 3.14.2 
- Unittest

## Guía de despliegue:

Este software no requiere de ningún tipo de instalación, simplemente clonando el repositorio y
ejecutando el programa main.py se realizan las pruebas incluidas en el código.

### Clonado y ejecución:

```bash
git clone https://github.com/catodevops/tarea_online_5.git
cd tarea_online_5
python main.py
```

## Tabla de trazabilidad

| Versión | Referencia Commit | Cambios realizados |
|---------|-------------------|--------------------|
|v0.1-----|6ef1ce1------------|Inicialización del proyecto|
|v0.2-----|12aecd9------------|Creación de branch desarrollo-seguro|
|v1.0-----|e381e05------------|Implementación del código funcional, README y .gitignore|

## Checklist de seguridad

Este proyecto contiene un archivo .gitignore donde se especifican una serie de carpetas y
archivos excluidos a la hora de subir cambios, los cuales están relacionados principalmente
con la higiene del repositorio. En mi caso he decidido ignorar un archivo cambios.txt que se encuentra en mi equipo local, sin ninguna razón técnica aparte de demostrar el correcto funcionamiento de .gitignore. Para el resto de exclusiones, el razonamiento es el siguiente:


- `__pycache__/`
Dado que contiene archivos de caché generados automáticamente por Python que no resultan útiles.
- `*.pyc`
Dado que contiene archivos automáticamente compilados de Python.
- `.vscode/`
Dado que contiene la configuración local de Visual Studio Code, que es el entorno que he utilizado.


Todos estos archivos son excluidos dado que no aportan ningún tipo de funcionalidad al programa:
- Son generados automáticamente por el entorno de trabajo utilizado
- Podría causar conflictos con ciertas máquinas
- Excluirlos hace más legible el contenido del repositorio
- Se considera mala práctica subir archivos no vitales y potencialmente problemáticos a un repositorio.
