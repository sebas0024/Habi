🏘️ API de Consulta de Propiedades - Prueba Técnica Habi

Esta solución proporciona una interfaz de servicios para la consulta del catálogo de propiedades inmobiliarias, permitiendo filtrado dinámico y visualización de la información más reciente mediante lógica de estados.

🛠️ Stack Tecnológico

- Backend: FastAPI & Uvicorn.
- Base de Datos: MySQL (vía MySQL Connector).
- Frontend: HTML5, JavaScript (ES6+) y CSS.

📁 Estructura del Proyecto

- backend/: Lógica de la API, conexión a base de datos y endpoints de consulta.
- frontend/: Interfaz de usuario, estilos y scripts de consumo de datos.

🚀 Instalación y Ejecución

1. Configuración del Entorno Virtual

Crear el entorno virtual

- python -m venv venv

Activar el entorno
En Windows (PowerShell):

- venv\Scripts\activate

En macOS/Linux:

- source venv/bin/activate

Nota para Windows: Si recibes un error de permisos al activar el entorno, ejecuta el siguiente comando en tu terminal de PowerShell:
- Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

2. Instalación de Dependencias

- pip install uvicorn fastapi mysql-connector-python

3. Puesta en marcha del Servidor

- python -m uvicorn backend.main:app --reload

4. Acceso a las Interfaces

- Validar API (Swagger): http://127.0.0.1:8000/docs
- Interfaz de Usuario (Frontend): http://127.0.0.1:5500/frontend/html/index.html


🧠 Desafíos Durante el Ejercicio

- Lógica de Base de Datos: El mayor desafío consistió en estructurar consultas SQL que filtraran correctamente el estado más reciente de cada propiedad, evitando mostrar registros históricos duplicados.
- Manejo de Parámetros: Se implementó una lógica flexible para recibir y procesar filtros opcionales (ciudad, año, estado) sin afectar el rendimiento de la consulta principal.
- Configuración del Entorno: Se gestionaron conflictos de puertos locales y se configuraron políticas de CORS para permitir la comunicación fluida entre el backend y el frontend.

🌐 Funcionalidades Clave

- Filtros Dinámicos: Búsquedas por ciudad, año y estado (Pre-venta, En venta, Vendido).
- Interfaz Responsiva: Diseño de tarjetas horizontales optimizado para web y móvil.
- Imágenes Inteligentes: Asignación automática de fachadas mediante el ID de cada propiedad.
- Formateo Local: Precios mostrados en formato de moneda colombiana (es-CO).


🚀 Extensión: Servicio de "Me gusta" (Conceptual)

Se diseñó una extensión del modelo de datos para permitir que los usuarios registrados interactúen con los inmuebles mediante un sistema de "Me gusta" o favoritos.

📊 Diseño del Modelo Entidad-Relación

Para cumplir con los requerimientos, se extendió la base de datos original incorporando dos nuevas entidades:

- users: Almacena la información de los usuarios registrados en la plataforma. Es la base para garantizar que solo usuarios autenticados realicen interacciones.
- likes: Funciona como una tabla relacional (muchos a muchos) que vincula a un usuario con una propiedad específica.

💡 Reglas de Negocio Implementadas

- Restricción de Usuario: La integridad referencial (Foreign Key hacia la tabla users) asegura que no existan interacciones de usuarios no registrados.
- Interacción: Se definió una llave única compuesta (user_id, property_id) que impide que un usuario registre más de un "Me gusta" sobre el mismo inmueble.
- Trazabilidad Histórica: La inclusión del campo created_at en la tabla de relación permite reconstruir el historial cronológico de favoritos de cada usuario.

🛠️ SQL de Extensión (Propuesta)

CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(64) UNIQUE NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL
);

CREATE TABLE likes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    property_id INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(id),
    CONSTRAINT fk_property FOREIGN KEY (property_id) REFERENCES property(id),
    UNIQUE (user_id, property_id)
);