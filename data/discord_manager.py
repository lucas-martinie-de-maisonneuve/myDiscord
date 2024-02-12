from data.database import Database
from datetime import datetime

class Discord_Manager(Database):
    def __init__(self):
        # Database.__init__(self, 'localhost', 'root', '$~Bc4gB9', 'discord')
        # Database.__init__(self, 'localhost', 'root', 'VannyLamorte25!', 'discord')
        Database.__init__(self, 'localhost', 'root', 'azerty', 'discord')
        self.connect()

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
        self.executeQuery(sql, values)

    def display_category(self):
        sql = "SELECT * FROM category"
        return self.fetch(sql)

    def add_channel(self, name, status, communication, id_category):
        sql = "INSERT INTO channel (name, status, communication, id_category) VALUES (%s, %s, %s, %s)"
        values = (name, status, communication, id_category)
        self.executeQuery(sql, values)

    def display_channel(self):
        sql = "SELECT * FROM channel"
        return self.fetch(sql)

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

    def check_credentials(self, nickname, password):
        sql = "SELECT * FROM user WHERE pseudo = %s AND password = %s"
        values = (nickname, password)
        user = self.fetch(sql, values)
        return user is not None  

    def save_message(self, name, message, id_channel):
        time = datetime.now()
        sql = "INSERT INTO message (name, time, message, id_channel) VALUES (%s, %s, %s, %s)"
        values = (name, time, message, id_channel)
        self.executeQuery(sql, values)

    def get_message(self):
        sql = "SELECT * FROM message"
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
manager.display_category()
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