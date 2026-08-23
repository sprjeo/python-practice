students = [
    {
        "name": "Anna",
        "grades": [5, 4, 5, 5, 4]
    },
    {
        "name": "Ivan",
        "grades": [3, 4, 3, 4, 3]
    },
    {
        "name": "Maria",
        "grades": [5, 5, 5, 4, 5]
    },
    {
        "name": "Petr",
        "grades": [4, 3, 4, 4, 3]
    },
    {
        "name": "Elena",
        "grades": [5, 4, 5, 4, 5]
    }
]

def get_stud_names(stud):
    res = []
    for x in stud:
        res.append(x['name'])
    return res 

def avg(stud, name):
    for x in stud:
        if x['name'] == name:
            return round(sum(x['grades'])/len(x['grades']),2)
    return


def get_stud_avgs(stud):
    res = {}
    for x in stud:
        res[x['name']] =  avg(stud, x['name'])
    return res

def get_best_stud(stud):
    best = next(iter(stud[0].values()))
    for x in stud:
        if  avg(stud, x['name']) > avg(stud, best):
            best = x['name']
    return best

def get_worst_stud(stud):
    worst = next(iter(stud[0].values()))
    for x in stud:
        if  avg(stud, x['name']) < avg(stud, worst):
            worst = x['name']
    return worst

def get_all_excellent_stud(stud):
    res = []
    for x in stud:
        if avg(stud, x['name']) >= 4.5:
            res.append(x['name'])
    return res

def get_overall_avg(stud):
    all_grades = []
    for x in stud:
        all_grades.extend(x['grades'])
    return round(sum(all_grades)/len(all_grades) , 2)

def get_num_of_students(stud):
    res = 0
    for x in stud:
        res += 1
    return res

def quantity_of_each_grade(stud):
    all_grades = []
    res = {}
    for x in stud:
        all_grades.extend(x['grades'])
    for x in all_grades:
        if x in res:
            res[x] += 1
        else:
            res[x] = 1
    return res


