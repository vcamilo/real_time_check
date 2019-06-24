#! /bin/python

from flask import (
        Flask,
        render_template,
        jsonify,
        request,
        )
import conexao
import time
import random

app = Flask(__name__)
con = conexao.Consulta()

@app.route('/', methods=['GET'])
def inicio():
    return render_template('index.html')

@app.route('/request', methods=['POST'])
def retorna_dados():
    lista = []
    dici = {}
    info = len(request.get_data())
    for i in range(info):
        lista.append(i)
    dici['lista'] = lista
    time.sleep(random.randint(0,3))
    return jsonify(dici)


if(__name__ == '__main__'):
        app.run(debug=True, host='0.0.0.0')
