import pandas as pd
import mysql.connector
from mysql.connector import Error

# ------------------- Cargar datos -------------------#

# Cargar datos del menú
df_menu = pd.read_csv('Cleaned_Menu.csv')
df_menu = df_menu[0:100]


# Cargar datos de la preparación
df_preparacion = pd.read_csv('Cleaned_Preparacion.csv')
df_preparacion = df_preparacion[0:100]

# ------------------- Conexión a la base de datos -------------------#
def connect_db(): 
    try:
        connection = mysql.connector.connect(
            host='localhost',  
            user='root',
            password='',
            database='proyecto'
        )
        if connection.is_connected():
            print('Conexión exitosa.')
            return connection
    except Error as e:
        print("Error al conectar a MySQL", e)

def upload_data(connection, df, table_name):
    cursor = connection.cursor()
    # Preparar sentencia SQL para insertar datos
    placeholders = ", ".join(["%s"] * len(df.columns))
    columns = ", ".join(df.columns)
    sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    for _, row in df.iterrows():
        cursor.execute(sql, tuple(row))
    connection.commit()
    cursor.close()
    
# Conexión a la base de datos
connection = connect_db()
    
# Subir datos a la base de datos
upload_data(connection, df_menu, 'menu')
upload_data(connection, df_preparacion, 'preparacion')
    
# Cerrar la conexión
if connection.is_connected():
    connection.close()
    print('Conexión cerrada.')