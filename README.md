# Proyecto-final-Rodriguez


## Tabla de contenidos

- [Descripción general](#descripción-general)
- [Aplicaciones](#aplicaciones)
  - [Blogs](#blogs)
  - [Accounts](#accounts)
  - [Messages](#messages)
- [Instalación](#instalación)
- [Uso](#uso)
- [Demostración](#demostracion)

## Descripción general

Este proyecto Django incluye tres aplicaciones principales: `blogs`, `accounts` y `messages`.

## Aplicaciones

### Blogs

La aplicación `blogs` permite a los usuarios ver, crear y comentar publicaciones. Las principales funciones incluyen:

- Listado de publicaciones destacadas y búsqueda de publicaciones.
- Visualización de detalles de una publicación.
- Creación de nuevas publicaciones.
- Comentar en publicaciones existentes.

### Accounts

La aplicación `accounts` se encarga del registro de nuevos usuarios.

### Messages

La aplicación `messages` permite a los usuarios:

- Ver una lista de mensajes.
- Visualizar detalles de un mensaje.
- Crear nuevos mensajes.
- Eliminar mensajes existentes.

## Instalación

1. Clonar el repositorio:

git clone https://github.com/your_username/your_repository.git

2. Crear un entorno virtual e instalar las dependencias:

cd your_repository
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

3. Aplicar las migraciones y crear la base de datos:

python manage.py makemigrations
python manage.py migrate

4. Ejecutar el servidor de desarrollo:

Una vez que el servidor esté en funcionamiento, puede acceder a las siguientes URL:

- Página principal: http://localhost:8000/
- Registro de usuario: http://localhost:8000/accounts/signup/
- Lista de mensajes: http://localhost:8000/messages/
- Crear nuevo mensaje: http://localhost:8000/messages/new/

## Demostración

Para ver el funcionamiento de la aplicacion puedes entrar al siguiente [link](https://www.google.com)