from flask import Flask, render_template, request
import google.generativeai as genai
import os
import markdown
from dotenv import load_dotenv
app = Flask(__name__)

load_dotenv()
url = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=url)
type_of_gemini = genai.GenerativeModel(
    'gemini-2.5-flash'
)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/sobre-equipe")
def equipe():
    return render_template("sobre_equipe.html")


@app.route("/certifications/aws")
def aws():
    return render_template("certifications/aws_cloud.html")


@app.route("/certifications/google_analytics")
def google():
    return render_template("certifications/google_analytics.html")


@app.route("/certifications/pcep")
def pcep():
    return render_template("certifications/pcep.html")


@app.route("/gemini", methods=["GET", "POST"])
def gemini_page():
    gemini_response = None
    comunication_error = None

    if request.method == "POST":
        user_question = request.form.get("question")

        if not user_question:
            comunication_error = "Por favor, digite uma pergunta!"
        else:
            try:
                context = "Você é um assistente especialista em certificações para desenvolvedores. Você deve ter conhecimento sobre AWS, Google Analytics e PCEP. Responda à pergunta do usuário de forma direta, concisa e utilizando o formato Markdown. Tente iniciar a resposta com um parágrafo normal, evitando símbolos como ` ou # na primeira linha. Se pedir para gerar uma tabela de preços, os items vazios coloque um '-'. "
                complete_prompt = context + user_question

                response = type_of_gemini.generate_content(
                    complete_prompt,
                )
                gemini_response = response.text

            except Exception as error:
                comunication_error = f"Não foi possível proceder com a pergunta. Erro encontrado {error}"


    return render_template(
        "gemini_page.html",
        gemini_response=gemini_response,
        comunication_error=comunication_error
    )


if __name__ == "__main__":
    app.run(debug=True)