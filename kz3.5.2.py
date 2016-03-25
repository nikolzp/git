from datetime import datetime
import csv
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

def find_oldest_person(filname):
    age_name = {}
    fp = open(filname)
    fp_csv = (csv.reader(fp))
    fp_csv.next()
    for a in fp_csv:
        each_person = Person(a[0],a[1],a[2])
        age_name.update({each_person.get_age():[a[0],a[1]]})
    old_age_name = age_name[max(age_name.keys())]
    return ' '.join(old_age_name)
         
