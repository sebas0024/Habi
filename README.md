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
source venv/bin/activate

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