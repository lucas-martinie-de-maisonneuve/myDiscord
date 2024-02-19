from datetime import datetime
from data.database import Database

class Discord_Manager(Database):
    def __init__(self):
        Database.__init__(self, 'localhost', 'root', '$~Bc4gB9', 'discord')
        # Database.__init__(self, 'localhost', 'root', 'VannyLamorte25!', 'discord')
        # Database.__init__(self, 'localhost', 'root', 'azerty', 'discord')
        self.connect()

    def check_credentials(self, email, password):
        sql = "SELECT * FROM user WHERE email = %s AND password = %s"
        values = (email, password)
        user = self.fetchone(sql, values)
        return user is not None
    
    def get_user(self, email, password):
        sql = "SELECT * FROM user WHERE email = %s AND password = %s"
        values = (email, password)
        user = self.fetchone(sql, values)
        return user
    
    def add_user(self, surname, name, pseudo, email, password, photo, id_role):
        sql = "INSERT INTO product (surname, name, pseudo, email, password, photo, id_role) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (surname, name, pseudo, email, password, photo, id_role)
        self.executeQuery(sql, values)

    def surname_user(self):
        sql = "SELECT surname FROM user"
        return self.fetch(sql)

    def display_user(self):
        sql = "SELECT * FROM user"
        return self.fetch(sql)

    def display_role_name(self):
        sql = "SELECT role.name FROM role LEFT JOIN user ON user.id_role = role.id"
        return self.fetch(sql)

    def add_category(self, name, intro):
        sql = "INSERT INTO category (name, intro) VALUES (%s, %s)"
        values = (name, intro)
        self.cursor.execute(sql, values)
        self.connection.commit()

    # Toutes Categories
    def display_category(self):
        sql = "SELECT * FROM category"
        self.cursor.execute(sql)
        self.categorys = self.cursor.fetchall()
        return self.categorys
    
    def count_category(self):
        sql = "SELECT COUNT(*) AS nb FROM category"
        self.cursor.execute(sql)
        nb = self.cursor.fetchone()
        return nb
    
    def id_category(self):
        sql = "SELECT id FROM category"
        self.cursor.execute(sql)
        self.categorys = self.cursor.fetchall()
        return self.categorys

    def name_category(self):
        sql = "SELECT name FROM category"
        self.cursor.execute(sql)
        self.categorys = self.cursor.fetchall()
        return self.categorys

    # Ajout Channel
    def add_channel(self,name,status,communication,id_category):
        sql = "INSERT INTO channel (name,status,communication,id_category) VALUES (%s, %s,%s, %s)"
        values = (name,status,communication,id_category)
        self.cursor.execute(sql, values)
        self.connection.commit()

    def display_channel(self):
        sql = "SELECT * FROM channel"
        self.cursor.execute(sql)
        self.channels = self.cursor.fetchall()
        return self.channels

    def name_channel(self,id):
        sql = "SELECT name FROM channel WHERE id_category = %s"
        values = (id,)
        self.cursor.execute(sql,values)
        self.channels = self.cursor.fetchall()
        return self.channels
    
    def count_channel(self):
        sql = "SELECT COUNT(*) AS nb FROM channel"
        self.cursor.execute(sql)
        nb = self.cursor.fetchone()
        return nb
    
    def count_channel(self,id):
        sql = "SELECT COUNT(*) AS nb FROM channel WHERE id_category = %s"
        values = (id,)
        self.cursor.execute(sql,values)
        nb = self.cursor.fetchone()
        return nb
    
    def id_channel(self):
        sql = "SELECT id_category FROM channel"
        self.cursor.execute(sql)
        self.channels = self.cursor.fetchall()
        return self.channels

    def communication_channel(self, id_category):
        sql = "SELECT communication FROM channel WHERE id_category = %s"
        values = (id_category,)
        self.cursor.execute(sql, values)
        self.channels = self.cursor.fetchall()
        return self.channels 
    

    # Supprimer User
    def delete_user(self, id):
        sql = "DELETE FROM user WHERE id = %s"
        values = (id,)
        self.executeQuery(sql, values)

    def delete_category(self, id):
        sql = "DELETE FROM category WHERE id = %s"
        values = (id,)
        self.executeQuery(sql, values)

    def delete_channel(self, id):
        sql = "DELETE FROM channel WHERE id = %s"
        values = (id,)
        self.executeQuery(sql, values)

    def save_message(self, name, message, id_channel):
        time = datetime.now()
        sql = "INSERT INTO message (name, time, message, id_channel) VALUES (%s, %s, %s, %s)"
        values = (name, time, message, id_channel)
        self.executeQuery(sql, values)

    def get_message(self):
        sql = "SELECT * FROM message"
        return self.fetch(sql)

    def name_message(self):
        sql = "SELECT name FROM message"
        return self.fetch(sql)
    
    def time_message(self):
        sql = "SELECT time FROM message"
        return self.fetch(sql)

    def message_message(self):
        sql = "SELECT message FROM message"
        return self.fetch(sql)

    def id_channel_message(self):
        sql = "SELECT id_channel FROM message"
        return self.fetch(sql)

    def close_connection(self):
        self.disconnect()

    # Modifier Role
    # def modify_role(self, user_id, id_role):
    #     set_clause = ", ".join([f"{key} = '{value}'" for key, value in new_product.items()])
    #     sql = f"UPDATE product SET {set_clause} WHERE id = %s"
    #     self.cursor.execute(sql, (product_id,))
    #     self.connection.commit()
    
manager = Discord_Manager()
# manager.display_category()
# manager.add_user("surname", "name", "pseudo", "email", "password","photo","id_role")
# manager.surname_user()
# manager.display_user()
# manager.display_role_name()
# manager.add_category("name","intro")
# manager.add_channel("name","status","communication","id_category")
# manager.display_channel()
# manager.delete_user("id")
# manager.delete_category("id")
# manager.delete_channel("id")
# manager.name_channel()

