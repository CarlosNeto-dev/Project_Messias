from flask import Flask, render_template, abort

app = Flask(__name__)

# Rota principal (Página Inicial: '/')
@app.route('/')
def index():
    # Não há mais necessidade de passar a lista 'certificacoes', pois a parte de detalhes foi removida.
    return render_template("index.html")

# Rota para a página 'Gemini'
@app.route('/gemini')
def gemini_page():
    return render_template("gemini.html")

# Rota para a página 'Certificações' (usada na navbar)
@app.route('/certificacoes')
def certificacoes_page():
    return render_template("index.html")

# Rota para a página 'Sobre'
@app.route('/sobre')
def sobre_page():
    return render_template("sobre.html")

@app.route("/certificacoes/aws")
def aws_page():
    return render_template("aws.html")

@app.route("/certificacoes/google")
def google_page():
    return render_template("google.html")

@app.route("/certificacoes/scrum")
def scrum_page():
    return render_template("scrum.html")


if __name__ == "__main__":
    app.run(debug=True)