from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user_model
from flask import flash

class Listing:
    my_db="pants_schema"
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.type = data['type']
        self.trend= data['trend']
        self.description= data['description']
        self.stoked_val= data['stoked_val']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.creator=None

    # crud queries 

    # insert into
    @classmethod
    def save_listing(cls,data):
        query='''
            INSERT INTO listings(user_id, type, trend, description)
            VALUES(%(user_id)s, %(type)s, %(trend)s, %(description)s);
        '''
        results= connectToMySQL(cls.my_db).query_db(query, data)
        return results


    # select w/join (read all and read one)
    @classmethod
    def get_all_listings(cls):
        query='''
            SELECT * FROM listings
            JOIN users
            ON listings.user_id = users.id;
        '''
        results= connectToMySQL(cls.my_db).query_db(query)
        if results:
            all_listings=[]
            for row in results:
                one_listing=cls(row)

                user_data={
                    'id': row['users.id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'email': row['email'],
                    'password': ' ',
                    'created_at': row['users.created_at'],
                    'updated_at': row['users.updated_at']
                }
                one_listing.creator= user_model.User(user_data)
                all_listings.append(one_listing)
            return all_listings
        else:
            return []



    #update

    #delete