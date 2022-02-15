from praticagem import raspagem
from flask import Flask, render_template
from  lista import pratic



app = Flask(__name__)

@app.route('/')
def index():
    va = raspagem()
    listas = pratic['praticagem']
    return render_template('index.html', va=va, listas=listas)


if __name__ == '__main__':
    app.run(debug=True)

