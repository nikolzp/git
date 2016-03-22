from datetime import datetime
class Person(object):
    def __init__(self, surname, first_name, birth_date, nickname = None):
        self.surname = surname
        self.first_name = first_name
        self.birth_date = datetime.strptime(birth_date,"%Y-%m-%d").date()
        if nickname is None: self.nickname = surname
        else: self.nickname = nickname
    
    def get_fullname(self):
        return self.surname + ' ' + self.first_name
    
    def get_age(self):
        return str((datetime.today().date() - self.birth_date)/365)[:2]





