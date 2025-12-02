from logging import exception

from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
API_KEY_GENAI = "gemini_api_key"

client = genai.Client(api_key=API_KEY_GENAI)

pergunta = input("Digite sua pergunta sobre Python: ").strip()
try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
        You're a specialist teacher with Python language. You need to response questions about Python.
        If the question is not about Python, you response 'I dont know about that. Say something about Python!'
        Pergunta: {pergunta}
        Responda colocando em formato Markdown!
        """
    )
except Exception as e:
    print(f"\033[1;31mERRO! --> {e}\033[m")
else:
    print(response.text)


