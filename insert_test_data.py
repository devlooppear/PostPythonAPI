from api.database import connect

def insert_test_data():
    conn = connect()
    if not conn:
        print("Erro ao conectar ao banco de dados.")
        return

    try:
        with conn.cursor() as cursor:
            data = [
                ("Série de Teste 1", "Drama", 10, 2023),
                ("Série de Teste 2", "Comédia", 8, 2022),
                ("Série de Teste 3", "Ação", 12, 2021),
                ("Série de Teste 4", "Ficção Científica", 15, 2020),
                ("Série de Teste 5", "Suspense", 10, 2019),
            ]
            cursor.executemany("INSERT INTO series (title, genre, num_episodes, release_year) VALUES (%s, %s, %s, %s)", data)
            conn.commit()
            print("Valores de teste inseridos com sucesso.")
    except Exception as e:
        print(f"Erro ao inserir valores de teste: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    insert_test_data()
