from flask import Flask, request, render_template

app = Flask(__name__)
frutas = ["maçã", "banana", "laranja", "melancia", "uva", "mamão", "abacaxi"]

@app.route('/')

def home_page():

    return render_template("index.html", frutas_do_html=frutas)


@app.route('/pagina2')
def pagina2():
    return render_template('pagina2.html')
@app.route('/processar_fruta', methods=['POST'])
def processar_fruta():
    nome_da_fruta = request.form['nome']
    frutas.append(nome_da_fruta)
    return render_template("pagina2.html", frutas_do_html=frutas)

if __name__ == '__main__':
    app.run(debug=True)