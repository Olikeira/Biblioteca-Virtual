from flask import Flask, jsonify, request, render_template, session
from flask_cors import CORS
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import render_template
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, static_folder='static',template_folder='templates')
CORS(app)
app.secret_key = 'supersecretkey'  # chave secreta para a sessão


db_config = {
    'dbname': 'Biblioteca',
    'user': 'postgres',
    'password': '123',
    'host': 'localhost'
}

@app.route('/')
def index():
    return render_template('indexprojeto.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/register')
def register():
    return render_template('register.html')


# Função para conectar ao banco de dados
def connect_db():
    return psycopg2.connect(**db_config)

# Rota para listar os livros
@app.route('/livros', methods=['GET'])
def get_livros():
    conn = connect_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM Livros")
    livros = cur.fetchall()
    conn.close()
    return jsonify(livros)

# Rota para adicionar um novo livro
@app.route('/livros', methods=['POST'])
def add_livro():
    data = request.json
    titulo = data.get('titulo')
    autor = data.get('autor')
    genero = data.get('genero')
    ano_publicacao = data.get('ano_publicacao')
    copias_disponiveis = data.get('copias_disponiveis')

    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO Livros (titulo, autor, genero, ano_publicacao, copias_disponiveis) VALUES (%s, %s, %s, %s, %s)",
                    (titulo, autor, genero, ano_publicacao, copias_disponiveis))
        conn.commit()
        conn.close()
        return jsonify({"message": "Livro adicionado com sucesso"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#listar livros
@app.route('/livros/filtrar', methods=['GET'])
def filtrar_livros():
    filtro_titulo = request.args.get('filtroTitulo')
    filtro_autor = request.args.get('filtroAutor')
    filtro_genero = request.args.get('filtroGenero')

    sql = "SELECT * FROM Livros WHERE 1=1"

    if filtro_titulo:
        sql += " AND titulo LIKE %s"
        filtro_titulo = "%" + filtro_titulo + "%"
    else:
        filtro_titulo = None

    if filtro_autor:
        sql += " AND autor LIKE %s"
        filtro_autor = "%" + filtro_autor + "%"
    else:
        filtro_autor = None

    if filtro_genero:
        sql += " AND genero LIKE %s"
        filtro_genero = "%" + filtro_genero + "%"
    else:
        filtro_genero = None

    conn = connect_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(sql, [filtro for filtro in [filtro_titulo, filtro_autor, filtro_genero] if filtro])
    livros_filtrados = cur.fetchall()
    conn.close()

    return jsonify(livros_filtrados)


# Rota para registrar um novo empréstimo
@app.route('/livros/<int:livro_id>/emprestar', methods=['POST'])
def registrar_emprestimo(livro_id):
    conn = connect_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT copias_disponiveis FROM Livros WHERE id = %s", (livro_id,))
    result = cur.fetchone()
    
    if result and result['copias_disponiveis'] > 0:
        try:
            cur.execute("UPDATE Livros SET copias_disponiveis = copias_disponiveis - 1 WHERE id = %s", (livro_id,))
            conn.commit()
            conn.close()
            return jsonify({"message": "Empréstimo registrado com sucesso"}), 201
        except Exception as e:
            conn.close()
            return jsonify({"error": str(e)}), 500
    else:
        conn.close()
        return jsonify({"error": "Não há cópias disponíveis para empréstimo"}), 400

# Rota para devolver um livro
@app.route('/livros/<int:livro_id>/devolver', methods=['POST'])
def devolver_livro(livro_id):
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("UPDATE Livros SET copias_disponiveis = copias_disponiveis + 1 WHERE id = %s", (livro_id,))
        conn.commit()
        conn.close()
        return jsonify({"message": "Livro devolvido com sucesso"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
