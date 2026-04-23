# 🏘️ API de Consulta de Propiedades - Prueba Técnica Habi

Esta solución proporciona una interfaz de servicios para la consulta del catálogo de propiedades inmobiliarias, permitiendo filtrado dinámico y garantizando la visualización de la información más reciente mediante lógica de estados históricos.

## 🛠️ Stack Tecnológico
Se implementó un ecosistema de herramientas de alto rendimiento, validadas bajo un entorno virtual aislado:

- **Núcleo de Servicios**: **FastAPI (v0.136.0)**. Encargado de la gestión de rutas y procesamiento de peticiones asíncronas.
- **Capa de Persistencia**: **MySQL Connector Python (v9.6.0)**. Driver utilizado para la comunicación directa y ejecución de sentencias SQL.
- **Interfaz de Servidor**: **Uvicorn (v0.45.0)**. Motor encargado de mantener el servicio activo y gestionar el tráfico HTTP.