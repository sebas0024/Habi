from backend.querys.request import fetch_properties

# Servicio encargado de manejar la lógica de negocio relacionada a propiedades
def get_properties(city=None, status=None, year=None):
    # Delega la consulta al repository (acceso a base de datos)
    return fetch_properties(city, status, year)