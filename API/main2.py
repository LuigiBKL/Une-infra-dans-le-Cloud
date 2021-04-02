import psycopg2
from config import config

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
        #data = cls.cur.fetchone()
        print(data)
        cls.close_connexion()
        return (data)

DataAccess.get_facilities()
