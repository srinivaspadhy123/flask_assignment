from flask_login import UserMixin

class User(UserMixin):
    def __init__(self,id,name,city,state):
        self.id = id
        self.name = name
        self.city = city
        self.state = state