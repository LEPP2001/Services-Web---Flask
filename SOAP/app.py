from flask import Flask, render_template
from flask import request
from flask import jsonify

app=Flask(__name__)

@app.route('/')
def users_action():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port="5000")    
