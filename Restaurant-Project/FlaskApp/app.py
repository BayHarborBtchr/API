from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

def load_data(file_name, nrows=8000):
    # Ruta completa al archivo CSV
    file_path = os.path.join(os.path.dirname(__file__), '..', 'transferencia', file_name)
    # Leer solo los primeros nrows datos
    df = pd.read_csv(file_path, nrows=nrows)
    return df

@app.route('/')
def index():
    # Cargar los datos de los diferentes archivos CSV
    menu_data = load_data('Cleaned_Menu.csv')
    preparacion_data = load_data('Cleaned_Preparacion.csv')
    
    # Pasar los datos a la plantilla
    return render_template('index.html',
                           menu_table=menu_data.to_html(classes='data'),
                           preparacion_table=preparacion_data.to_html(classes='data'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999, debug=True)

