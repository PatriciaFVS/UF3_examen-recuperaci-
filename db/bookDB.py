from db import clientPS

#Per passar dades i esquemetitzar en format JSON:
def bookSchema(book) ->dict:
    return {"title": book[0],
            "author":book[1],
            "published at":str(book[2]),
            "genre":book[3],
            "language": book[4],
            "pages": str(book[5]),
            "created_at": str(book[6]),
            "updated_at": str(book[7]),
            
        
    }

#Obtenir tots els registres de la taula book
def consultaTots():
    try:
        #connexió amb la base de dades
        conn = clientPS.client()
        #executa connexió amb cursor
        cur=conn.cursor()
        #query
        cur.execute("SELECT * FROM public.book")
        #recuperar tots els registres
        data= cur.fetchall()
    except Exception as e:
        print(f'Error connexió {e}')
    
    finally:
        conn.close
        for dat in data: 
            return bookSchema(dat)

#Afegir un nou registre
def add(llib):
    try:
        conn = clientPS.client()
        cur=conn.cursor()
        cur.execute(f"INSERT INTO public.book (id, title, author, published_year, genre, language, pages) VALUES ('{llib.id}','{llib.title}', '{llib.author}',{llib.published_year}, '{llib.genre}', '{llib.language}',{llib.pages})")
        conn.commit()
        return "Llibre afegit correctament"
    except Exception as e:
        print(f'Error connexió {e}')
    finally:
        conn.close
        
#Eliminar registre
def delete(id):
    try:
        conn = clientPS.client()
        cur=conn.cursor()
        cur.execute(f"DELETE FROM public.book WHERE id = {id}")
        conn.commit()
        
    except Exception as e:
        print(f'Error connexió {e}')
    finally:
        conn.close
        return {"message": "S'ha eliminat correctament"}