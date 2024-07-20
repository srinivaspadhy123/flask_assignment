class DbModel:
    def __init__(self,id=None,name=None,city=None,state=None):
        self.id = id
        self.name = name
        self.city = city
        self.state = state

    def set_id(self,id):
        self.id = id

    def set_name(self,name):
        self.name = name
    
    def set_city(self,city):
        self.city = city

    def set_state(self,state):
        self.state = state

    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name
    
    def get_city(self):
        return self.city
    
    def get_state(self):
        return self.state