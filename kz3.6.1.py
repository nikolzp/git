class Student(object):
    def __init__(self, name, conf={'lab_max':0, 'lab_num':0}):
        self.name = name
        self.conf = conf
        self.labs = [a*0 for a in range(self.conf.get("lab_num"))]
    
    def set_lab(self, score, number = None):
        if number is None:
            self.labs[0] = score
        else:
            self.labs[number] = score
        return self.labs
     
    def average_score(self):
        okruglenie = sum(self.labs)/float(len(self.labs))
        return round(okruglenie, 1)
    
    
    
ivan = Student("Ivan", {"lab_max": 5, "lab_num": 4})
print ivan.labs
print ivan.set_lab(4, 1)
print ivan.set_lab(5)
print ivan.average_score()
print ivan.set_lab(3)
