import csv
class Student(object):
    def __init__(self, name, conf={'lab_max':0, 'lab_num':0}):
        self.name = name
        self.conf = conf
        self.labs = [a*0 for a in range(self.conf.get("lab_num"))]
    
    def set_lab(self, score, number = None):
        self.number = number
        if len(self.labs) < self.number:
            return 'error'
        if score > self.conf.get("lab_max"):
            score = self.conf.get("lab_max")
        if number is None:
            if 0 in self.labs:
                self.labs[self.labs.index(0)] = score
            else: 
                return 'error' 
        else:
            self.labs[number] = score
        return self.labs
     
    def average_score(self):
        okruglenie = sum(self.labs)/float(len(self.labs))
        return round(okruglenie, 1)


def find_best_student(filename):
    dic = {} 
    fp = open(filename)
    fp.readline()
    fp_csv = csv.reader(fp)
    for a in fp_csv:
        s = Student(a[0], {'lab_max':int(a[1]), 'lab_num':int(a[2])})
        for r in range(s.conf.get('lab_num')):
            ma = {s.name: sum(s.set_lab(int(a[r+3]), r))}
            dic.update(ma)
    fp.close()
    name_val = max(dic.values())
    name = [a for a in dic if dic[a]==name_val]
    return name[0]
    


p = find_best_student('student.csv')
print p

