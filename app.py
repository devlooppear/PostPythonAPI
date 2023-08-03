from flask import Flask, request, jsonify
from api.database import connect
import json

app = Flask(__name__)

@app.route('/series', methods=['GET'])
def get_series():
    conn = connect()
    if not conn:
        return jsonify({"message": "Erro ao conectar ao banco de dados."}), 500

    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM series")
            series = cursor.fetchall()
            return json.dumps({"series": series}, ensure_ascii=False), 200, {'Content-Type': 'application/json; charset=utf-8'}
    except Exception as e:
        print(f"Erro ao buscar séries: {e}")
        return jsonify({"message": "Erro ao buscar séries no banco de dados."}), 500
    finally:
        conn.close()

@app.route('/series/<int:id>', methods=['GET'])
def get_series_by_id(id):
    conn = connect()
    if not conn:
        return jsonify({"message": "Erro ao conectar ao banco de dados."}), 500

    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM series WHERE id = %s", (id,))
            series = cursor.fetchone()
            if series:
                return jsonify({"series": series})
            else:
                return jsonify({"message": "Série não encontrada."}), 404
    except Exception as e:
        print(f"Erro ao buscar série: {e}")
        return jsonify({"message": "Erro ao buscar série no banco de dados."}), 500
    finally:
        conn.close()

@app.route('/series', methods=['POST'])
def add_series():
    conn = connect()
    if not conn:
        return jsonify({"message": "Erro ao conectar ao banco de dados."}), 500

    try:
        data = request.get_json()
        title = data.get('title')
        genre = data.get('genre')
        num_episodes = data.get('num_episodes')
        release_year = data.get('release_year')

        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO series (title, genre, num_episodes, release_year) VALUES (%s, %s, %s, %s) RETURNING id",
                           (title, genre, num_episodes, release_year))
            new_id = cursor.fetchone()[0]
            conn.commit()
            return jsonify({"message": "Série adicionada com sucesso.", "id": new_id}), 201
    except Exception as e:
        print(f"Erro ao adicionar série: {e}")
        conn.rollback()
        return jsonify({"message": "Erro ao adicionar série no banco de dados."}), 500
    finally:
        conn.close()

@app.route('/series/<int:id>', methods=['PUT'])
def update_series(id):
    conn = connect()
    if not conn:
        return jsonify({"message": "Erro ao conectar ao banco de dados."}), 500

    try:
        data = request.get_json()
        title = data.get('title')
        genre = data.get('genre')
        num_episodes = data.get('num_episodes')
        release_year = data.get('release_year')

        with conn.cursor() as cursor:
            cursor.execute("UPDATE series SET title = %s, genre = %s, num_episodes = %s, release_year = %s WHERE id = %s",
                           (title, genre, num_episodes, release_year, id))
            conn.commit()
            return jsonify({"message": "Série atualizada com sucesso."}), 200
    except Exception as e:
        print(f"Erro ao atualizar série: {e}")
        conn.rollback()
        return jsonify({"message": "Erro ao atualizar série no banco de dados."}), 500
    finally:
        conn.close()

@app.route('/series/<int:id>', methods=['DELETE'])
def delete_series(id):
    conn = connect()
    if not conn:
        return jsonify({"message": "Erro ao conectar ao banco de dados."}), 500

    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM series WHERE id = %s", (id,))
            conn.commit()
            return jsonify({"message": "Série excluída com sucesso."}), 200
    except Exception as e:
        print(f"Erro ao excluir série: {e}")
        conn.rollback()
        return jsonify({"message": "Erro ao excluir série no banco de dados."}), 500
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
