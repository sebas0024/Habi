from backend.querys.request import fetch_properties

def get_properties(city=None, status=None, year=None):
    return fetch_properties(city, status, year)