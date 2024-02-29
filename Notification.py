import datetime, json
from source.pygame_manager.Element import Element

class Notification(Element):    

    def __init__(self): 
        Element.__init__(self)
        self.last_login_date = self.load_last_login_date()

    def load_last_login_date(self):
        try:
            with open("notification.json", "r") as json_file:
                data = json.load(json_file)
                return datetime.datetime.fromisoformat(data["last_login"])
            
        except FileNotFoundError:
            return datetime.datetime.min

    def save_last_login_date(self, date):
        with open("notification.json", "w") as json_file:
            json.dump({"last_login": date.isoformat()}, json_file)
            
    def display_notification(self, nb_notification):
        self.text_not_align(self.font1, 20, nb_notification, self.red, 1075, 30)