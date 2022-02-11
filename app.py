from praticagem import raspagem
from flask import Flask, render_template



app = Flask(__name__)

@app.route('/')
def index():
    va = raspagem()
    return render_template('index.html', va=va)


if __name__ == '__main__':
    app.run(debug=True)

