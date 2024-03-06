import mysql.connector

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.userdb = user
        self.password = password
        self.database = database

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.userdb,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.connection.close()

    def execute_query(self, query, params=None):
        self.connect()
        self.cursor.execute(query, params or ())
        self.connection.commit()
        self.disconnect()

    def fetch(self, query, params=None):
        self.connect()
        self.cursor.execute(query, params or ())
        result = self.cursor.fetchall()
        self.disconnect()
        return result
        
    def fetch_one(self, query, params=None):
        self.connect()
        self.cursor.execute(query, params or ())
        result = self.cursor.fetchone()
        self.disconnect()
        return result
    
# if __name__ == '__main__':
#     db = Database('localhost', 'root', 'VannyLamorte25!', 'discord')
#     query = "SELECT audio_blob FROM audio WHERE id = %s"
#     values = (14,)
#     save = db.fetch(query, values)[0][0]
#     with open("output1.wav", 'wb') as f:
#         f.write(save)