#Inicializar libreria/dependencias
from flask import Flask
from flask import render_template
from flask import request

import os

app = Flask(__name__)

#rutas 
@app.route('/', methods=['GET', 'POST'])
def inicio():
    return render_template('index.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run("0.0.0.0", port=port, debug=True)