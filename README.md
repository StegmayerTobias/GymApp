# GymApp
Aplicación para gym con autenticación. Django + JS

## Instalación
### Crear un entorno virtual
python -m venv venv
### Activar el entorno
venv\Scripts\activate

O en Visual Studio, click en f1
>Python Select Interpreter
Y cambiar al que dice venv

### Instalar dependencias
pip install -r requirements.txt

## Ejecución
python manage.py runserver

## Superusuario
Crear superusuario para entrar al perfil del staff

python manage.py createsuperuser 

Superusuario de prueba:

email: staff1@gmail.com

contraseña: 123
