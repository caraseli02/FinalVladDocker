#Inicializar libreria/dependencias
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

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
collection2 = db['Client']

#rutas 
@app.route('/', methods=['GET', 'POST'])
def inicio():
    content = {}
    total = float()
    if request.method == 'POST':
        mes = request.form.get('mes')
        combustible = float(request.form.get('combustible'))
        recambios = float(request.form.get('recambios'))
        renting = float(request.form.get('renting'))
        seguro = float(request.form.get('seguro'))
        if combustible == "":
            return render_template('index.html')
        total = combustible + recambios + renting + seguro

        collection.delete_many({})
        collection.insert_one({"content": {
            "mes" : mes,
            "combustible" : combustible,
            "recambios" : recambios,
            "renting" : renting,
            "seguro" : seguro,
            "total" : total
        }})
        content = {
            "mes" : mes,
            "combustible" : combustible,
            "recambios" : recambios,
            "renting" : renting,
            "seguro" : seguro,
            "total" : total
        }
        return render_template('index.html', **content)
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    content = {}
    if request.method == 'POST':
        passw = request.form.get('pass')
        mail = request.form.get('mail')
        resultado = list(collection2.find({"mail" : mail}))
        if mail in resultado:
            return render_template('Login.html', resultado=resultado, mail=mail)
    return render_template('Login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    content = {}
    if request.method == 'POST':
        km = request.form.get('km')
        marticula = request.form.get('marticula')
        passw = request.form.get('pass')
        mail = request.form.get('mail')

        collection2.insert_one({
            "km": km,
            "marticula": marticula,
            "password": passw,
            "mail": mail
        })
        content = {
            "km": km,
            "marticula": marticula,
            "password": passw,
            "mail": mail
        }
        return render_template('register.html', **content)
    return render_template('register.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run("0.0.0.0", port=port, debug=True)