from flask import Flask, render_template
from flask import request
from flask import jsonify

app=Flask(__name__)

@app.route('/')
def users_action():
    materias= ['Mantenimiento', 'Sis. Distribuidos', 'Adm. Proyectos', 'Vis. Artificial']
    data={
        'titulo': 'Index',
        'bienvenida': 'Saludos',
        'materias': materias,
        'numMaterias': len(materias)
    }
    
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, port="5000")    
