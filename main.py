#importacions

from fastapi import FastAPI
from db import bookDB
from model.book import Book
app=FastAPI()

#rutes
@app.get("/llibres/getall/")
def getBook():
    data=bookDB.consultaTots()
    return (data) 

@app.post("/llibres/add/")
def addBook(llibre:Book):
    data=bookDB.add(llibre)
    return (data)

@app.delete("/llibres/delete/{id}")
def delBook(id:int):
    data=bookDB.delete(id)
    return (data)