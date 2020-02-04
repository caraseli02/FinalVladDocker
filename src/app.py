#Inicializar libreria/dependencias
from flask import Flask
from flask import render_template
from flask import request

import os

# Paquete para Base de datos
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Mongo URL Atlas
MONGO_URL_ATLAS = 'mongodb+srv://admin:root@cluster0-odxe4.mongodb.net/test?retryWrites=true&w=majority'

client = MongoClient(MONGO_URL_ATLAS, ssl_cert_reqs=False)
db = client['Coche']
collection = db['Gastos']

#rutas 
@app.route('/', methods=['GET', 'POST'])
def inicio():
    content = {}
    if request.method == 'POST':
        mes = request.form.get('mes')
        combustible = float(request.form.get('combustible'))
        recambios = float(request.form.get('recambios'))
        renting = float(request.form.get('renting'))
        seguro = float(request.form.get('seguro'))

        content = {
            "mes" : mes,
            "combustible" : combustible,
            "recambios" : recambios,
            "renting" : renting,
            "seguro" : seguro
        }
        return render_template('index.html', **content)
    return render_template('index.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run("0.0.0.0", port=port, debug=True)