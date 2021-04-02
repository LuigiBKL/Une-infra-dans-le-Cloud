from cassandra.cluster import Cluster

class DataAccess():


    cluster = Cluster(['localhost'],port=9042)
  
    @classmethod
    def connexion(cls):
    #if __name__ == "__main__":
        
        session = cls.cluster.connect('resto',wait_for_all_pools=True)
        return session
   
    @classmethod
    def fermer_connexion(cls):
        
        cls.cluster.shutdown()
    
    @classmethod
    def get_info_id(cls,id):
        
        info_resto_id = {}
        liste_info_resto_id = []
        session = cls.connexion()
        session.execute('USE resto')
        # rows = session.execute('SELECT * FROM restaurant')
        rows = session.execute(f'SELECT id, borough, buildingnum,cuisinetype,phone,street,name,zipcode  FROM restaurant WHERE id={id};')
        for row in rows:
            print(row.zipcode,row.street,row.phone,row.borough,row.id,row.cuisinetype)
            info_resto_id = {'id':row.id,'borough':row.borough,'buildingnum':row.buildingnum,'cuisinetype':row.cuisinetype,'phone':row.phone,'street':row.street,"name":row.name,'zipcode':row.zipcode}
            liste_info_resto_id.append(row)
        print(info_resto_id)
        #fermer_connexion(cluster)

        return liste_info_resto_id
    
    @classmethod
    def get_info_kitchen(cls,cuisinetype):
        
        info_restaurant = {}
        cuisinetype = str(cuisinetype)
        session = cls.connexion()
        session.execute('USE resto')
        #rows = session.execute('SELECT * FROM restaurant WHERE cuisinetype="Mexican";')
        rows = session.execute(f"SELECT * FROM restaurant WHERE cuisinetype= '{cuisinetype}';")
        for row in rows:
            #print(row.zipcode,row.street,row.phone,row.borough,row.id,row.cuisinetype)
            info_restaurant = {'id':row.id,'nom':row.name,'rue':row.street}
        print(info_restaurant)
        #fermer_connexion(cluster)
        return info_restaurant
    
    @classmethod
    def get_info_inspection(cls,idrestaurant):
            
            info_inspection = {}
            session = cls.connexion()
            session.execute('USE resto')
            #rows = session.execute('SELECT * FROM restaurant WHERE cuisinetype="Mexican"')
            rows = session.execute(f"SELECT score,idrestaurant,violationdescription  FROM inspection WHERE idrestaurant = {idrestaurant} ;")
            for row in rows:
                print(row.idrestaurant,row.score,row.violationdescription)
                info_inspection = {'id_restaurant':row.idrestaurant,'score':row.score,'violationdescription':row.violationdescription}
            #fermer_connexion(cluster)
            return info_inspection

    @classmethod
    def get_ten_resto(cls, grade):
        
        dico ={}
        idrestaurant = []
        liste_grade = []
        #grade = str(grade)
        session = cls.connexion()
        session.execute('USE resto')
        rows = session.execute(f"SELECT idrestaurant FROM inspection WHERE grade= '{grade}' GROUP BY idrestaurant limit 10;")
        for row in rows:
            #print(row.idrestaurant,row.score,row.violationdescription)
            idrestaurant.append(row.idrestaurant)
        for id in idrestaurant:
                info = session.execute(f"SELECT name  FROM restaurant WHERE id = {id};")
                info = list(info)
                dico = {id:info}
                liste_grade.append(dico)

        #print (info)
        #fermer_connexion(cluster)
        return liste_grade


#DataAccess().get_info_id(50006392)
# print('===========================================')
#resto = DataAccess().recup_info_type_cuisine('Thai') 
# print('===========================================')
#DataAccess().get_info_inspection(50006392)
# print('===========================================')
# print(resto)
grade = DataAccess().get_ten_resto('A')
print(grade)