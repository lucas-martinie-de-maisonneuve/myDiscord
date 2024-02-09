from data.database import Database
class Discord_Manager(Database):
    def __init__(self):
        # Database.__init__(self, 'localhost', 'root', '$~Bc4gB9', 'discord')
        Database.__init__(self, 'localhost', 'root', 'azerty', 'discord')
        # Database.__init__(self, 'localhost', 'root', '$~Bc4gB9', 'discord')
        self.connect()
        self.cursor = self.connection.cursor()
        
    # Ajout Utilisateur
    def add_user(self, surname, name, pseudo, email, password,photo,id_role):
        sql = "INSERT INTO user (surname, name, pseudo, email, password,photo,id_role) VALUES (%s, %s, %s, %s, %s,%s,%s)"
        values = (surname, name, pseudo, email, password,photo,id_role)
        self.cursor.execute(sql, values)
        self.connection.commit()

    # Nom Utilisateur
    def surname_user(self):
        sql = "SELECT surname FROM user"
        self.cursor.execute(sql)
        self.names = self.cursor.fetchall()
        return self.names
    
    # Tout Utilisateurs
    def display_user(self):
        sql = "SELECT * FROM user"
        self.cursor.execute(sql)
        self.users = self.cursor.fetchall()
        return self.users
    
    # Nom Role Utilisateur 
    def display_role_name(self):
        sql = "SELECT role.name FROM role LEFT JOIN user ON user.id_role = role.id"
        self.cursor.execute(sql)
        self.name_role = self.cursor.fetchall()
        return self.name_role
    
    # Ajout Categorie
    def add_category(self,name,intro):
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
    
    # Ajout Channel
    def add_channel(self,name,status,communication,id_category):
        sql = "INSERT INTO channel (name,status,communication,id_category) VALUES (%s, %s,%s, %s)"
        values = (name,status,communication,id_category)
        self.cursor.execute(sql, values)
        self.connection.commit()

    # Toutes Channels
    def display_channel(self):
        sql = "SELECT * FROM channel"
        self.cursor.execute(sql)
        self.channels = self.cursor.fetchall()
        return self.channels
    
    # Supprimer User
    def delete_user(self, id):
        sql = "DELETE FROM user WHERE id = %s"
        values = (id,)
        self.cursor.execute(sql, values)
        self.connection.commit()
        
    # Supprimer Category
    def delete_category(self, id):
        sql = "DELETE FROM category WHERE id = %s"
        values = (id,)
        self.cursor.execute(sql, values)
        self.connection.commit()
        
    # Supprimer Channel
    def delete_channel(self, id):
        sql = "DELETE FROM channel WHERE id = %s"
        values = (id,)
        self.cursor.execute(sql, values)
        self.connection.commit()
    
    # Modifier Role
    # def modify_role(self, user_id, id_role):
    #     set_clause = ", ".join([f"{key} = '{value}'" for key, value in new_product.items()])
    #     sql = f"UPDATE product SET {set_clause} WHERE id = %s"
    #     self.cursor.execute(sql, (product_id,))
    #     self.connection.commit()
    
    def close_connection(self):
        self.cursor.close()
        self.connection.close()

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