from math import ulp


def your_future_age(name, age):
    return print(f'Hello,{name}! In 5 years you will be {int(age)+5} years old')

#user_name = input('enter your name: ')
#user_age = input('enter your age: ')
#your_future_age(user_name, user_age)

def parity(num):
    if num%2==0:
        return print ('even')
    else:
        return print ('odd')
#test_num = input('enter number you want to test on parity: ')
#parity(int(test_num))

def find_max(a):
    var = 0
    for i in range(len(a)):
         if a[i]>var:
             var=a[i]
    return var

#rand_list = [1, 143, 32, 213, 22]
#print(rand_list, find_max(rand_list), max(rand_list))

def op_with_list(a):
    asum = 0
    amax=amid=amin=a[0]
    for i in range(len(a)):
        if a[i]>amax:
            amax=a[i]
        if a[i]<amin:
            amin=a[i]
        asum+=a[i]
    return print(f'summary = {asum} {sum(a)}  mean = {asum/len(a)} maximum = {amax} {max(a)} mimimum = {amin} {min(a)}')


#numbers = [4, 7, 2, 9, 12, 5, 8]
#op_with_list(numbers)

def filtration(a):
    over_10 = list()
    only_even = list()
    for i in range(len(a)):
        if a[i]>10:
            over_10.append(a[i])
        if a[i]%2==0:
            only_even.append(a[i])
    return over_10, only_even

#numbers = [12, 5, 8, 21, 3, 17, 10, 4, 25]
#print(filtration(numbers))

def op_with_str(s):
    len(s)
    words = s.split()
    return print(f'number of characters: {len(s)}, number of words: {len(words)}, string in uppercase: {s.upper()}, string in lowercase: {s.lower()}, first word is {words[0]}')

#user_str = input('enter your sentense: ')
#op_with_str(user_str)


def print_dict(dict):
    for key, value in dict.items():
       print(f'{key}: {value}')
    return print('\n')

#student = {
#    "name": "Anna",
#    "age": 22,
#    "university": "MSU",
#    "grade": 4.7
#}
#
#print_dict(student)
#student['speciality'] = 'Applied Mathematics and Computer Science'
#print_dict(student)

def task_10():
    user_list = range(1,101)
    sum = 0
    for num in user_list:
        if num%3 == 0:
            sum+=num
    return sum

#print(task_10())
def task_11():
    numbers = [1, 5, 8, 10, 13, 17, 20]
    up_5, under_18, even = [] , [] , []
    for x in numbers:    
        if x > 5:
            up_5.append(x)
        if x < 18:
            under_18.append(x) 
        if x%2 == 0:
            even.append(x)
    return up_5, under_18, even

#print(task_11())

def is_prime(num):
    if num <= 1:
        return False
    for i in range(num**0.5 + 1):
        if num%i==0:
            return False
    return True

def count_vowels(text):
    vowels = 'aeyuio'
    count = sum(1 for char in text.lower() if char in vowels)
    return count

#print(count_vowels("hello"))

def task_14():
    grades = [5, 4, 3, 5, 4, 5, 2, 4, 5, 3]
    return print(f'maen = {round(sum(grades)/len(grades))}\
    5 count = {(sum(1 for num in grades if num==5))} \
    4 count = {(sum(1 for num in grades if num==4))} \
    3 count = {(sum(1 for num in grades if num==3))} \
    2 count = {(sum(1 for num in grades if num==2))}')

#task_14()