# GymApp

Aplicación para gym con autenticación de usuario. Modulo para staff y modulo para alumnos.

## Tecnologías

- **HTML**
- **CSS** 
- **JavaScript** 
- **django**

## Instalación

Clona el repositorio localmente.

Crea un entorno virtual y activalo.

```bash
  python -m venv venv
 
  venv/Scripts/activate
```

O en Visual Studio, click en f1, **">Python Select Interpreter"**, cambiar al que dice **venv**.

Instalar dependencias

```bash
 pip install -r requirements.txt
```

## Ejecución

```bash
 python manage.py runserver
```

## Superusuario
Superusuario de prueba:

- email: staff@gmail.com

- contraseña: 1234
  
O crear un nuevo superusuario para entrar al perfil del staff

```bash
 python manage.py createsuperuser 
```

