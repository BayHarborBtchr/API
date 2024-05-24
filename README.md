# API

### Guía de Ejecución del Proyecto

Este documento proporciona una guía paso a paso sobre cómo construir y ejecutar el proyecto usando Docker y Docker Swarm.

#### Requisitos Previos

- Docker
- Docker Compose

#### Pasos para Ejecutar el Proyecto

1. **Clonar el repositorio**

   Clona el repositorio del proyecto en tu máquina local:

   ```sh
   git clone https://github.com/BayHarborBtchr/API.git
   cd API/Restaurant-Project
   ```

2. **Construir las imágenes de Docker**

   Navega al directorio raíz del proyecto y construye las imágenes de Docker para cada servicio. Asegúrate de estar en el directorio correcto donde se encuentra el archivo `docker-compose.yml`.

   ```sh
   docker-compose build
   ```

3. **Desplegar la pila de servicios en Docker Swarm**

   Inicializa Docker Swarm si no lo has hecho antes:

   ```sh
   docker swarm init
   ```

   Luego, despliega la pila de servicios utilizando Docker Swarm:

   ```sh
   docker stack deploy -c docker-compose.yml stack1
   ```

4. **Verificar que los servicios están en ejecución**

   Verifica que todos los servicios están en ejecución utilizando el siguiente comando:

   ```sh
   docker service ls
   ```

   Asegúrate de que todos los servicios tengan el estado `1/1 REPLICAS`.

5. **Acceder a la aplicación web**

   Una vez que todos los servicios estén en ejecución, puedes acceder a la aplicación web desde tu navegador en la siguiente URL:

   ```
   http://localhost:2080
   ```

### Descripción de los Servicios

1. **Base de Datos (MySQL)**

   - **Nombre del Servicio**: `stack1_db`
   - **Imagen**: `mysql:5.7`
   - **Puerto**: `32000 -> 3306/tcp`

2. **Servicio de Facturas**

   - **Nombre del Servicio**: `stack1_facturas`
   - **Imagen**: `blwmi/facturas:latest`
   - **Puerto**: `3003 -> 3003/tcp`

3. **Servicio de Inventario**

   - **Nombre del Servicio**: `stack1_inventario`
   - **Imagen**: `blwmi/inventario:latest`
   - **Puerto**: `3002 -> 3002/tcp`

4. **Servicio de Transferencia**

   - **Nombre del Servicio**: `stack1_transferencia`
   - **Imagen**: `blwmi/transferencia:latest`

5. **Servicio de Usuarios**

   - **Nombre del Servicio**: `stack1_usuarios`
   - **Imagen**: `blwmi/usuarios:latest`
   - **Puerto**: `3001 -> 3001/tcp`

6. **Servicio Web**

   - **Nombre del Servicio**: `stack1_web`
   - **Imagen**: `blwmi/webpicco:latest`
   - **Puerto**: `2080 -> 80/tcp`

### Solución de Problemas

- **Ver los registros de un servicio**: Si necesitas ver los registros de un servicio para diagnosticar problemas, puedes usar el siguiente comando:

  ```sh
  docker service logs <nombre_del_servicio>
  ```

  Por ejemplo, para ver los registros del servicio de facturas:

  ```sh
  docker service logs stack1_facturas
  ```

- **Reiniciar un servicio**: Si un servicio no se está ejecutando correctamente, puedes reiniciarlo usando el siguiente comando:

  ```sh
  docker service update --force <nombre_del_servicio>
  ```

  Por ejemplo, para reiniciar el servicio de usuarios:

  ```sh
  docker service update --force stack1_usuarios
  ```


Esta guía debe ayudarte a ejecutar el proyecto y a solucionar cualquier problema que pueda surgir. Si tienes alguna duda adicional, no dudes en preguntar. 
