from flask import Flask, render_template, send_file
import sqlite3
import io

app = Flask(__name__)

# Função para conectar ao banco de dados e obter informações
def get_animais():
    conn = sqlite3.connect('dados_animais.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, peso FROM animais")
    animais = cursor.fetchall()
    conn.close()
    return animais

# Rota para a página principal, onde os dados serão listados
@app.route('/')
def index():
    animais = get_animais()
    return render_template('index.html', animais=animais)

# Rota para exibir a imagem de uma pessoa
@app.route('/foto/<int:id>')
def foto(id):
    conn = sqlite3.connect('dados_animais.db')
    cursor = conn.cursor()
    cursor.execute("SELECT foto FROM animais WHERE id=?", (id,))
    foto_blob = cursor.fetchone()[0]
    conn.close()

    # Enviar a imagem como resposta binária
    return send_file(io.BytesIO(foto_blob), mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)
