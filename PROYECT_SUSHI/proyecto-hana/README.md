# proyecto-hana

## Que es nuestro proyecto?:

 ### HANA
 La empresa ficticia HANA desea lanzar su tienda online para vender sus productos por delivery y take away. Necesitan una plataforma web que permita a los clientes navegar en el catalogo de productos, ver detalles de cada plato, registrarse, iniciar sesion y realizar compras. Los administradores podran cargar y modificar productos, ver pedidos, y gestionar stock. Los usuarios podran agregar productos al carrito de compras y efecturar la compra.

## Participantes:
- Candela Esquitin
- Agustina Lemos
- Agustina Rudman
- Juan Jose Rojas
- Luciana Sanchez
- Susana Cai
- Maria Fernanda Rivera de la Cruz
- Valentina Romero

## Levantamiento del proyecto:
Se tienen como opciones "pipenv" y "venv" como entornos virtuales para el levantamiento del proyecto.
Para facilitar el proceso se tiene el script "setup.sh" que recibe ambas opciones como parámetro para su ejecución y crea el entorno virtual correspondiente. Para que el mismo se puede ejecutar se requiere utilizar "chmod +x setup.sh" previamente.
Finalizada la ejecución del script, se debe activar el entorno virtual como corresponda, ya sea con "pipenv shell" si se levantó con "pipenv" o con "source .venv/bin/activate" si se hizo con "venv".
Para la visualización de la página se debe ejecutar "python3 src/app.py" luego de la activación del entorno virtual.