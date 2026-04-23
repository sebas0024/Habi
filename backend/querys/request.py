from backend.db.connection import get_connection

def fetch_properties(city=None, status=None, year=None):

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

    params = []

    if city:
        query += " AND p.city = %s"
        params.append(city)

    if status:
        query += " AND s.name = %s"
        params.append(status)

    if year:
        query += " AND p.year = %s"
        params.append(year)

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, params)

    return cursor.fetchall()