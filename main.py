#! /bin/python

from flask import (
        Flask,
        render_template,
        jsonify,
        request,
        )
import conexao

app = Flask(__name__)
con = conexao.Base()

@app.route('/', methods=['GET'])
def inicio():
    return render_template('teste.html')

@app.route('/request', methods=['POST'])
def retorna_dados():
    info = request.get_data().strip('/{%}*\\_()[]&~|$<>')
    if(len(info) > 6):
        result = con.consulta(info)
        return jsonify(result)
    return jsonify('')

if(__name__ == '__main__'):
        app.run(debug=True, host='0.0.0.0')
