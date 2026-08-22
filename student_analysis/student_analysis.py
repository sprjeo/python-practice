
students = [
    {"name": "Anna", "grades": [5, 4, 5, 5, 4]},
    {"name": "Ivan", "grades": [3, 4, 3, 4, 3]},
    {"name": "Maria", "grades": [5, 5, 5, 4, 5]},
    {"name": "Petr", "grades": [4, 3, 4, 4, 3]},
    {"name": "Elena", "grades": [5, 4, 5, 4, 5]},
]
#print([list(x.values()) for x in students ])

def average_grade(idict):
    for x in idict:
        stud = list(x.values())
        name = stud[0]
        grades = stud[1]
        average = round(sum(grades)/len(grades),1)
    
        print(name,':', average)
    return    

def best_stud(idict):
    best_grade = 0
    best = ''
    for x in idict:
        stud = list(x.values())
        name = stud[0]
        grades = stud[1]
        average = round(sum(grades)/len(grades),1)
        if average>best_grade:
            best = name
            best_grade = average

    return print(f'Best student: {best}\nAverage grade: {best_grade}')

def worst_stud(idict):
    worst_grade = 5
    worst = ''
    for x in idict:
        stud = list(x.values())
        name = stud[0]
        grades = stud[1]
        average = round(sum(grades)/len(grades),1)
        if average<worst_grade:
            worst = name
            worst_grade = average

    return print(f'Worst student: {worst}\nAverage grade: {worst_grade}')

def group_average(idict):
    all_grades = 0
    grades_counter = 0
    for x in idict:
        stud = list(x.values())
        grades = stud[1]
        all_grades += sum(grades)
        grades_counter += len(grades)
    return print (f'Group average: {all_grades/grades_counter}' )

def excellent_stud_counter(idict):
    counter = 0
    for x in idict:
        stud = list(x.values())
        grades = stud[1]
        average = round(sum(grades)/len(grades),1)
        if average >= 4.5:
            counter += 1
    return counter

def excellent_students(idict):
    print('Excellent students:')
    for x in idict:
        stud = list(x.values())
        name = stud[0]
        grades = stud[1]
        average = round(sum(grades)/len(grades),1)
        if average >= 4.5:
            print('- ',name)
    return


def menu():
    opt = 1
    while opt != 0:
        print('===== Student Analysis ===== \n\n1. Show all students\n2. Show best student\n3. Show worst student\n4. Show group average\n5. Show excellent students\n0. Exit\n')
        opt = int(input('Choose an option: '))
        if opt < 0 or opt > 5:
            print('wrong input\n')
            opt = input('Choose an option again(from 0 to 5): ')
        elif opt == 1:
            average_grade(students)
        elif opt == 2:
            best_stud(students)
        elif opt == 3:
            worst_stud(students)
        elif opt == 4:
            group_average(students)
        elif opt == 5:
            excellent_students(students)
        else:
           return
        print('\n')

    return


menu()