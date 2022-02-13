from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Users:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_assignment').query_db(query)
        users = []
        for u in results:
            users.append( cls(u) )
        return users

    @classmethod
    def save(cls, data) :
        query = "INSERT INTO users ( first_name , last_name , email, created_at) VALUES ( %(first_name)s, %(last_name)s, %(email)s, NOW(), NOW();"
        result = connectToMySQL('users_assignment').query_db( query, data )
        return result
