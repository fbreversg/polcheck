# POLCHECK-APP
API REST que permite:

 - Consultar políticos
 - Crear político (y relaciones)
 - Actualizar el partido (y relación) de un político
 - Importar un csv para popular la BD

Adicionalmente permite:

 - Consultar un politico
 - Borrar un politico

---
Desarrollo en FLASK + FLASK_RESTFUL apoyado en BD NEO4J con plugin de auto-uuid (https://github.com/graphaware/neo4j-uuid)

Python 3.7+

---
## Instruccciones de instalación

 - pip install -r requirements.txt
 - Crear base de datos de NEO4J y modificar las siguientes settings
   (Neo4j configuration)
   
* Comentar para poder cargar CSVs desde fuera de la carpeta por defecto.
> #dbms.directories.import=import
* Añadir al final para activar el auto UUID
> com.graphaware.runtime.enabled=true
com.graphaware.module.UIDM.1=com.graphaware.module.uuid.UuidBootstrapper

 - Añadir a la carpeta plugins de la BD los dos jars que permiten la generación de UUIDs.
 -- GraphAware UUID : http://products.graphaware.com/download/uuid/latest
 -- GraphAware Framework : http://products.graphaware.com/download/framework-server-community/latest
---

## Configuracion

**config.py**

Permite configurar la carpeta donde se alojará el csv y tamaño máximo.

>UPLOAD_DIR = '/tmp'

>MAX_UPLOAD_SIZE = 16 * 1024 * 1024  # 16MB

**Variables de entorno para conectividad con NEO4J**

Es necesario exportar las siguientes variables para la conexion con BD y definir entorno de FLASK.

* NEO4J_PASSWORD
* NEO4J_USER
* NEO4J_URI
* FLASK_ENV

Ej (*NIX):

> EXPORT NEO4J_PASSWORD=1234

> EXPORT NEO4J_USER=neo4j

> EXPORT NEO4J_URI=bolt://localhost:7687

> EXPORT FLASK_ENV=development

---

## OPERACIONES API

- POST /import Import CSV.
- GET /index Mostar un listado con 50 políticos
- PUT /update/[uuid]/partido/[nombrePartido] Cambiar un político de partido y su relación
- POST /create Añadir un nuevo político con sus relaciones

## OPERACIONES API RESTFUL

- GET    /polcheck/politicos
- GET    /polcheck/politicos/[uuid]
- POST   /polcheck/politicos
- PUT    /polcheck/politicos/[uuid]/partido/[nombrePartido]
- DELETE /polcheck/politicos/[uuid]

Ejemplos de uso en la coleccion de POSTMAN: https://github.com/fbreversg/polcheck/blob/master/postman_tests/PolCheck.postman_collection.json

## ToDo

- Generar links (identidad, borrado, update...) en las respuestas del API RESTFUl.
- Generar pruebas en la coleccion de POSTMAN.
- Tests BDD.
- Creacion de nodos en la importacion en una sola query para evitar la relectura.
- Incluir documentacion SWAGGER.
- Probar otro tipo de generacion de UUID unico para evitar el problema del lazy creation.
