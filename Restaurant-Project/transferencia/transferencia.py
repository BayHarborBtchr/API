import pandas as pd
import mysql.connector
from mysql.connector import Error
import os

# ------------------- Cargar datos -------------------#

# Cargar datos del menú
df_menu = pd.read_csv('Cleaned_Menu.csv')
df_menu = df_menu[0:100]

# ------------------- Conexión a la base de datos -------------------#
def connect_db(): 
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST', 'db'),
            user=os.getenv('DB_USER', 'root'),
            password=os.getenv('DB_PASSWORD', 'root'),
            database=os.getenv('DB_NAME', 'proyecto')
        )
        if connection.is_connected():
            print('Conexión exitosa.')
            return connection
    except Error as e:
        print("Error al conectar a MySQL", e)
        return None

def upload_data(connection, df, table_name):
    if connection is None:
        print("Conexión no establecida, no se pueden subir los datos.")
        return

    cursor = connection.cursor()
    # Preparar sentencia SQL para insertar datos
    placeholders = ", ".join(["%s"] * len(df.columns))
    columns = ", ".join(df.columns)
    sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    for _, row in df.iterrows():
        cursor.execute(sql, tuple(row))
    connection.commit()
    cursor.close()
    print(f"Datos insertados en la tabla {table_name}")
    
# Conexión a la base de datos
connection = connect_db()

# Subir datos a la base de datos si la conexión fue exitosa
if connection:
    upload_data(connection, df_menu, 'menu')
    
    # Cerrar la conexión
    if connection.is_connected():
        connection.close()
        print('Conexión cerrada.')
