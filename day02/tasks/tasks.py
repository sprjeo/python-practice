#=================================Block 2=================================#

student = {
    "name": "Anna",
    "age": 22,
    "university": "MSU",
    "grade": 4.7
}

def get_name(stud):
    return stud['name']
def get_grade(stud):
    return stud['grade']
def change_age(stud):
    new_age=input('enter update age: ')
    stud['age']= new_age
    return 

student['speciality'] = 'Applied Mathematics'
del student['university']

def check_email(stud):
    if 'email' in stud:
        return True
    return False

#print(student)

#print(f'{student.keys()}\n {student.values()}\n {student.items()}')

def print_all_keys(stud):
    for x in stud:
        print(x)
    return

#print_all_keys(student)

def print_all_values(stud):
    for x in stud.items():
        print(stud[x])
    return

#print_all_values(student)

def print_pairs(stud):
    for key, value in stud.items():
        print(f'{key} -> {value}')
    return

#print_pairs(student)

#students = {
#    "Anna": [5, 4, 5, 5],
#    "Ivan": [3, 4, 3, 4],
#    "Maria": [5, 5, 5, 4]
#}

def get_average(stud,name):
    if name in stud:
        grades = stud[name]
        return round((sum(grades)/len(grades)),2)
    return
#print(get_average(students,'Anna'))

def get_all_avg(stud):
    avgs={}
    for x in stud:
        avgs[x] = get_average(stud,x)
    return avgs

#print_pairs((get_all_avg(students)))

def get_best_student(stud):
    best = 0
    best_stud = ''
    for x in stud:
        if get_average(stud,x)>best:
            best_stud = x
    return best_stud

#print(get_best_student(students))

def get_all_excellent_stud(stud):
    exc_stud = []
    for x in stud:
        if get_average(stud,x) >= 4.5:
            exc_stud.append(x)
    return exc_stud

#print(get_all_excellent_stud(students))


#=================================Block 3=================================#

students = [
    {
        "name": "Anna",
        "age": 22,
        "grades": [5, 4, 5, 5]
    },
    {
        "name": "Ivan",
        "age": 23,
        "grades": [3, 4, 3, 4]
    },
    {
        "name": "Maria",
        "age": 21,
        "grades": [5, 5, 5, 4]
    }
]

def print_names(stud):
    for x in stud:
        print(x['name'])
    return

def print_over_21(stud):
    for x in stud:
        if x['age'] > 21:
            print(x['name'])
    return

def get_avg(stud, name):
    for x in stud:
        if x['name'] == name:
            return round(sum(x['grades'])/len(x['grades']),2)
    return


def get_all_avgs(stud):
    avgs = {}
    for x in stud:
        avgs[x['name']] = get_avg(stud,x['name'])
    return avgs

#print_pairs(get_all_avgs(students))

def get_best(stud):
    best = ''
    best_avg = 0
    for x in stud:
        if get_avg(stud,x['name'])>best_avg:
            best = x['name']
    return best

def get_overall_avg(stud):
    all_grades = []
    for x in stud:
        all_grades.extend(x['grades'])
    return round(sum(all_grades)/len(all_grades),2)

#print(get_overall_avg(students))


#=================================Block 4=================================#


numbers = [1, 2, 3, 4, 5, 6, 7, 8]

result = []

#result = [x**2 for x in numbers]
#result = [x  for x in numbers if x%2==0]
#result = [x**2 for x in numbers if x%2==0]


words = ["python", "data", "math", "model", "sql"]
#result = [len(x) for x in words]
result = [x for x in words if len(x)>4]

#print(result)


#=================================Block 5=================================#


def calculate_average(num):
    return round(sum(num)/len(num),2)

#result = calculate_average([1, 2, 3, 4, 5])
#print(result)

def get_even_numbers(numbers):
    res = []
    for x in numbers:
        res.append(x)
    return res

def get_students_above_average(students, threshold):
    res = []
    for x in students:
        avg = get_avg(students, x['name'])
        if avg >= threshold:
            res.append(x['name'])
    return res

#print(get_students_above_average(students, 4.5))



#=================================Block 6=================================#


numbers = [7, 2, 9, 4, 2, 8, 7, 3, 9, 1]



def unique(numbers):
    res = []
    for x in numbers:
        if x in res:
            continue
        else:
            res.append(x)
    return res

#print(unique(numbers))

def num_of_num(numbers):
    res ={}
    for x in numbers:
        if x in res:
            res[x] += 1
        else:
            res[x] = 1
    return res

#print(num_of_num(numbers))

def most_frequent(numbers):
    num_dict = num_of_num(numbers)
    res = next(iter(num_dict))
    for x in numbers:
        if num_dict[x] > num_dict[res]:
            res = x
    return res

def sort_unique(numbers):
    res = unique(numbers)
    res.sort()
    return res

print(sort_unique(numbers))


