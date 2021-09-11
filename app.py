from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here


    fox_img= {}
    for elemento in range(5) :
        dados = requests.get('https://randomfox.ca/floof/').json()
        fox_img[elemento] = [dados['image']]



    return render_template('index.html', lista_fox=fox_img)


if __name__ == '__main__':
    app.run()
