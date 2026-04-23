from backend.db.connection import get_connection


# Función encargada de consultar propiedades desde la base de datos
def fetch_properties(city=None, status=None, year=None):

    """
    Consulta propiedades aplicando filtros opcionales y retorna su estado más reciente.

    Parámetros:
    - city (str): filtra por ciudad
    - status (str): filtra por estado de la propiedad (pre_venta, en_venta, vendido)
    - year (int): filtra por año de construcción

    Retorna:
    - Lista de diccionarios con la información de las propiedades
    """
    
    # Query principal:
    # - Obtiene propiedades
    # - Trae únicamente el último estado usando subconsulta
    # - Limpia datos (description vacía -> 'NA')
    # - Filtra propiedades válidas (price > 0, address y city no nulos)


    query = """
    SELECT 
        p.id,
        p.address,
        p.city,
        p.price,
        COALESCE(NULLIF(p.description, ''), 'NA') AS description,
        COALESCE(NULLIF(p.year, ''), 'NA') AS year,
        s.name AS status
    FROM property p
    JOIN status_history sh ON sh.property_id = p.id
    JOIN status s ON s.id = sh.status_id
    WHERE sh.id = (
        SELECT sh2.id
        FROM status_history sh2
        WHERE sh2.property_id = p.id
        ORDER BY sh2.update_date DESC, sh2.id DESC
        LIMIT 1
    )
    AND s.name IN ('pre_venta', 'en_venta', 'vendido')
    AND p.price > 0 and p.address IS NOT NULL and p.city IS NOT NULL
    """

    # Lista de parámetros para evitar SQL Injection
    params = []

    # Filtros dinámicos
    if city:
        query += " AND p.city = %s"
        params.append(city)

    if status:
        query += " AND s.name = %s"
        params.append(status)

    if year:
        query += " AND p.year = %s"
        params.append(year)

    # Conexión a la base de datos
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    # Ejecución segura de la query con parámetros
    cursor.execute(query, params)
    return cursor.fetchall()