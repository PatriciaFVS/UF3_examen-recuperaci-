import psycopg

def client():
    #connexió amb la base de dades
    conexio = """
                    dbname=uf3Examen
                    user=user_postgres
                    password=pass_postgres
                    host=localhost
                    port=5432
                """
    
    try:
        return psycopg.connect(conexio)

    except Exception as e:
        print(f"Hi ha hagut un error: {e}")