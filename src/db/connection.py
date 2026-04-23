import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="13.58.82.14",
        port=3309,
        user="pruebas",
        password="VGbt3Day5R",
        database="habi_db"
    )