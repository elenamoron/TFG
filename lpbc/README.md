# Ejecutar un proyecto Django con Docker y docker-compose

### Requisitos previos

Tener instalado Docker (**versión 17.12**) y docker-compose (**versión 1.18**)

Instalación de Docker - https://docs.docker.com/install/linux/docker-ce/ubuntu/

```
// En caso de tener docker instalado anteriormente.
$ sudo apt-get remove docker docker-engine docker.io
// Instalación
$ sudo apt-get update

$ sudo apt-get install     apt-transport-https     ca-certificates     curl     software-properties-common
    
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

// Verificar la clave
$ sudo apt-key fingerprint 0EBFCD88
// Inclusión del repositorio
$ sudo add-apt-repository    "deb [arch=amd64] https://download.docker.com/linux/ubuntu    $(lsb_release -cs)    stable"

$ sudo apt-get update
$ sudo apt-get install docker-ce
// Instalacion de una version concreta de Docker. En nuestro caso, utilizamos la versión 17.12.0-ce
$ sudo apt-get install docker-ce=<VERSION>
// Comprobamos que se ha instado correctamente.
$ sudo docker run hello-world

```

Post-Instalación de Docker (podremos ejecutar sin _sudo_) - https://docs.docker.com/install/linux/linux-postinstall/

```
// Al ejecutar el siguiente comando puede decirnos que ya existe el usuario
$ sudo groupadd docker
$ sudo usermod -aG docker $USER
// Tras este comando, debemos cerrar sesión y volver a entrar para que hagan efecto los cambios.
// Probamos otra vez, el hello world, esta vez, sin sudo.
$ docker run hello-world
```

Instalación de Docker-Compose - https://docs.docker.com/compose/install/ - https://github.com/docker/compose/releases
```
// Con este comando instalamos la versión 1.19 de Docker-Compose
curl -L https://github.com/docker/compose/releases/download/1.19.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
```

Comprobar qué contenedores están activos
```
$ docker ps
```

Listado de todos los contenedores Docker ejecutados y en ejecución.
```
$ docker ps -a
```

Borrado de contenedores
```
$ docker rm <id-contenedor>
```

Listar todas las images instaladas
```
$ docker images
```
Borrado de imagenes
```
$ docker rmi <nombre-de-imagen>
```

Ejecutar comandos dentro del contenedor
```
$ docker run <nombre-del-contenedor> ...
// Ejemplo
$ docker run web python manage.py ...
```
Utilizamos la nomenclatura _expose_ en lugar de _ports_ con el objetivo de no tener que parar
los servicios utilizados en local, como pueden ser _Redis_ o _MySQL_.

Se puede modificar al gusto del desarrollador.

### Primeros pasos

Clonar el repositorio:
```
git clone <repositorio> [nombre-del-repo-local]
```

Borrar directorio _.git_:
```
cd nombre-del-repo
ls -l
rm -rf .git/ 
```
Creación del virtualenv para evitar errores del intérprete de Python y Django
```
virtualenv -p python3[.6] venv
```
Renombrar el archivo _env.sample_ por _.env_. 
```
$ cp env.sample .env
```

Esto es necesario para ejecutar
el contenedor de Docker. Antes de ejecutar el docker-compose debemos rellenar 
el parámetro _SECRET_KEY_ del archivo _.env_.

Esto es necesario para ejecutar el contenedor de Docker. Antes de ejecutar el docker-compose 
debemos rellenar el parámetro _SECRET_KEY_ del archivo _.env_.

Para ejecutar este proyecto Django con Docker, escribimos en terminal:
```
$ docker-compose up
```
O en el caso de que no queramos bloquear el terminal:
```
$ docker-compose up -d
```
En el caso de que haya conflicto entre el MySQL interno y el MySQL de Docker, 
debido a la configuración de puertos. Tendremos que o bien, parar el servicio
de MySQL interno.
```
$ sudo service <nombre-del-servicio> stop
```
O bien, cambiando la configuración del puerto de salida, del _3306_, al _3307_, 
por ejemplo.


Este comando creará los contenedores de Docker que se especifican en el
archivo _docker-compose.yml_, además de lanzar su ejecución. 
Tras esto, y según indica nuestro _docker-compose.yml_, se ejecutará nuestra 
aplicación de Django en una instancia aislada, y podremos acceder a nuestra 
aplicación introduciendo la ruta _0.0.0.0:8000_ en el navegador.

Comprobar que los contenedores han sido lanzados se hace con el comando
`docker ps`. En el caso de que alguno de los contenedores no se haya 
ejecutado o queramos lanzar un servicio de forma individual, escribimos en 
 terminal `docker-compose up 
<nombre-del-servicio>`, de esta manera sabremos además, cual ha sido el 
error durante su ejecución.

Podemos reiniciar los contenedores con `docker-compose restart [nombre-contenedor]`
### Trabajar en local con nuestro proyecto Django

La existencia de un virtualenv local nos sirve de ayuda y guía mientras
desarrollamos un proyecto con Pycharm, por tanto, es recomendable la
creación de uno.

Además, muchos de los cambios que realizamos en nuestra aplicación no se 
propagan al contenedor de Docker que ejecutamos, por ejemplo, la instalacion 
de una nueva biblioteca o paquete. En caso de que queramos trabajar con el 
proyecto en local sin depender del contenedor de Docker, tenemos que:
1. Crear un virtualenv
2. Instalar los paquetes del archivo _requirements.txt_. 
(`pip install -r /path/to/requirements.txt`)
3. Añadir la cadena correspondiente al parámetro _SECRET_KEY_ del archivo
_settings.py_.

Todos los paquetes adicionales que instalemos, debemos añadirlos en nuestro
fichero de _requirements.txt_ para la posterior creación de la imagen del
contenedor _web_.


### Actualizar requirements en Docker y crear nueva imagen

Tener un virtualenv en local permite instalar, de forma aislada, los paquetes 
necesarios para el correcto funcionamiento de la aplicación.

Cada vez que añadimos uno o varios nuevos paquetes o bibliotecas a nuestra
aplicación, debemos "construir" de nuevo la imagen de nuestro proyecto en 
Django.

Para ello, ejecutamos:

```
pip freeze > /path/to/file/requirements.txt
docker-compose build
```

Si no realizamos _build_ y ejecutamos directamente `docker-compose up`, el 
contenedor ejecutará la imagen anterior sin los paquetes actualizados, por lo 
su funcionamiento puede no ser el deseado.

También podemos instalar las librerias en el contenedor directamente.

```
docker-compose run web bash
pip install <paquete-deseado>
pip freeze > /path/to/requirements.txt
exit
```

### Ejecución de pruebas

Ejecución de pruebas
```
docker-compose run web python manage.py test -v 2
```
De este modo obtenemos una traza de los tests realizados, además de poder ver la traza del 
error en caso de fallo.

### Analisis de cobertura

Instalamos mediante pip los paquetes _coverage_ y _django-nose_
```
pip install coverage
pip install django-nose
```

Tenemos que añadir ciertos parámetros de configuración para aplicar el analisis.

```
INSTALLED_APPS = (
    # ...
    'django_nose',
)

# Use nose to run all tests
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# Tell nose to measure coverage on the 'foo' and 'bar' apps
NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=<nombre/s-de-la/s-aplicacion/es>', //En nuestro caso, connector
    '--cover-html' //Muestra en formato HTML el analisis.
]
```

Para ejecutar los tests y el análisis de cobertura, escribimos:

```
docker-compose run web python manage.py test
```

Obtendremos una salida por consola del resultado de los tests y de los
analisis de cobertura, además de guardar el resultado de estos en un 
directorio _cover_ en la raíz de nuestra aplicación.

### Depurar ipdb en el proyecto dentro del contenedor Docker

Si deseamos controlar algunos errores que nos de la aplicación tenemos que
añadir las lineas:
```
import ipdb
ipdb.set_trace()
```

Depurar con ipdb dentro de los contenedores puede presentar dos escenarios,
uno en el cual depuramos cosas que se ejecutan como respuesta a operaciones 
con la web, y otro es depurar tests unitarios escritos por nosotros.

```
docker-compose stop web
docker-compose run --service-ports web python manage.py runserver 0.0.0.0:8000
docker-compose run --service-ports web python manage.py test
```

Continuar la ejecución del proyecto y/o de las pruebas tenemos que introducir
_c_ (continue), para continuar la ejecución. Si queremos comprobar el valor
de una variable, introducimos su nombre en el bash de ipdb.
 


### Activar extensión Pylint en proyecto

Para poder ejecutar la extensión de Pylint debemos realizar _pip install pylint_ con el entorno virtual activado.

Una vez instalada la biblioteca de Pylint podemos activarla en el entorno de _PyCharm_. Para ello tenemos que ir a 
File > Settings > Tools > External Tools y agregar una nueva en el botón __+__.

Como nombre le pondremos pylint. Más tarde será lo que identifique a la extensión a la hora de activarla, así que 
podemos escribir lo que queramos. Como program, ponemos la ruta que tenemos desde nuestro virtualenv, que suele ser 
virtualenv/bin/pylint. Por último, como parameters, introducimos '$FilePath$'. Por último, aceptamos y guardamos nuestra
extensión.

Para activarla y poder aplicarla en los archivos de nuestro proyecto, vamos a Tools > External Tools > Pylint. Tendremos
a nuestra disposición una pantalla para hacer el checkeo en cada archivo del proyecto y sólo tendremos que usar el
botón _play_.

### LDAP

Probar conexion
```
ldapwhoami -vvv -h <hostname> -p <puerto> -D <usuario> -x -w <password>
```

```
ldapsearch -h dc.i2tic.com -p 389 -D admin -w 4vXKyXC7wDAmX4NQxeGdnHeJmHqqxhhFRM9 -b 'dc=dc, dc=i2tic, dc=com' -s base 'objectClass=*' 1.1
```

```
ldapsearch -h dc.i2tic.com -p 389 -D admin -w 4vXKyXC7wDAmX4NQxeGdnHeJmHqqxhhFRM9 -b '' -s base 'objectClass=*' 1.1
```

Utilizar phpLDAPadmin:

```
docker run -p 6443:443 --env PHPLDAPADMIN_LDAP_HOSTS=dc.i2tic.com --detach osixia/phpldapadmin:0.7.1
```

En navegador, ir a la dirección: 

_https://localhost:6443_

Nos dirá que el sitio no es seguro, añadimos como excepción y nos saldrá la 
página principal de _phpLDAPadmin_.

##### Login con credenciales:
_Login_DN_: admin


_Password_: 4vXKyXC7wDAmX4NQxeGdnHeJmHqqxhhFRM9

- Cómo depurar con `ipdb`

Hay dos escenarios, uno es depurar cosas que se ejecutan como respuesta a 
operaciones con la web, y otro es depurar tests unitarios

```
docker-compose stop web
docker-compose run --service-ports web python manage.py runserver 0.0.0.0:8000
docker-compose run --service-ports web python manage.py test
```
