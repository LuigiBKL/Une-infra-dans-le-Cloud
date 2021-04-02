import psycopg2
from config import config
from importlib import reload
from typing import Optional
from fastapi import FastAPI
import uvicorn # ASGI server
#from data import DataAccess as da
from fastapi.encoders import jsonable_encoder
from urllib.parse import urlparse

class DataAccess():


  
    @classmethod
    def connexion(cls):
    
     #""" Connect to the PostgreSQL database server """
        conn = None
        
        try:
            # read connection parameters
            params = config()

            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect(**params)
        
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
        return conn 
    

   
    @classmethod
    def close_connexion(cls):
        
        cls.conn = cls.connexion()
        if cls.conn is not None:
            cls.conn.close()
            print('Database connection closed.')
    
    
    @classmethod
    def get_facilities(cls):
        cls.cur = cls.connexion().cursor()
        cls.cur.execute('SELECT * FROM cd.facilities')
        data = cls.cur.fetchall()
        print(data)
        cls.close_connexion()
        return (data)

    @classmethod
    def get_membercost(cls):
        cls.cur = cls.connexion().cursor()
        cls.cur.execute('SELECT * FROM cd.members')
        data = cls.cur.fetchall()
        #data = cls.cur.fetchone()
        #print(data)
        cls.close_connexion()
        return (data)

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Coucou Aws"}

@app.get("/get_facilities")
async def get_facilities():
    
    data = DataAccess().get_facilities()
    #DataAccess().deconnexion()
    return data

@app.get("/get_membercost")
async def get_membercost():
    
    data = DataAccess().get_membercost()
    #DataAccess().deconnexion()
    return data
# DataAccess.get_facilities()
