from flask import Flask, request, render_template
import openai

app = Flask(__name__)

chat = []


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        pregunta = request.form.get("pregunta")
        resultado = enviar_pregunta(pregunta)
        chat.append(("Yo", pregunta))
        chat.append(("ChatGPT", resultado))
    else:
        resultado = ""

    return render_template('index.html', chat=chat)


def enviar_pregunta(pregunta):
    openai.api_key = "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"
    respuesta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres una asistente útil."},
            {"role": "user", "content": pregunta}
        ],
    )
    respuesta_texto = respuesta["choices"][0]["message"]["content"]
    return respuesta_texto


if __name__ == "__main__":
    app.run(debug=True, port=5000)
