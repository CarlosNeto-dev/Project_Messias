import os
from flask import Flask, render_template, request
import google.generativeai as genai
import markdown

key_of_gemini = genai.configure(api_key="AIzaSyA811-hMyJ9RNWgTAku4q_xC4zftNNSLnw")

app = Flask(__name__)

# Development Environment
os.environ['FLASK_DEBUG'] = 'True'
app.debug = os.environ.get('FLASK_DEBUG') == 'True'

@app.route("/")
def index():
    return render_template("model.html")


@app.route("/gemini", methods=["GET", "POST"])
def gemini_assist_page():
    gemini_response = None
    if request.method == "POST":
        question = request.form.get("pergunta")
        if question:
            try:
                model = genai.GenerativeModel("gemini-2.5-flash")
                response = model.generate_content(question)

                if response and response.text:
                    gemini_response = response.text
                    gemini_response = markdown.markdown(gemini_response)
                else:
                    gemini_response = "❌ Erro na Resposta da API: A API retornou uma resposta vazia (None). Verifique se a sua chave de API é válida e se a pergunta não violou as diretrizes de conteúdo do Gemini."
            except Exception as e:
                gemini_response = f"❌ Erro na Comunicação: A API falhou por um motivo inesperado. Detalhes: {e}"

    return render_template("gemini_page.html", gemini_response=gemini_response)


if __name__ == '__main__':
    app.run()