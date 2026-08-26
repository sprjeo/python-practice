import pandas as pd
import matplotlib.pyplot as plt



#=================================Block 1=================================#
data = {
    "name": ["Anna", "Ivan", "Maria", "Petr", "Elena"],
    "age": [22, 23, 21, 24, 22],
    "math": [5, 4, 5, 3, 5],
    "programming": [4, 5, 4, 3, 4]
}

df = pd.DataFrame(data)

def task_1(df):
    return{
       "df": df, 
       "head": df.head(),
       "shape": df.shape,
       "columns": df.columns,
       "dtypes": df.dtypes,
       "describe": df.describe()     
    }

#for key, value in task_1(df).items():
#    print(f'{key}: \n{value}\n')


#=================================Block 2=================================#

def task_2(df):
    return{
        'df[\'name\']' : df["name"],
        'df[\'math\']' : df["math"],
        'df[[\'name\', \'math\']]' : df[["name", "math"]],
        'df[[\'math\']]' : df[["math"]],
        'df.iloc[0]' : df.iloc[0],
        'df.iloc[1]' : df.iloc[1],
        'df.iloc[:3]' : df.iloc[:3],    
        'df.loc[0]' : df.loc[0]
    }

#for key, value in task_2(df).items():
#    print(f'{key}: \n{value}\n')


#=================================Block 3=================================#


def task_3(df):
    return{
        'math >= 5' : df[df["math"] >= 5],
        'age > 22' : df[df['age'] > 22],
        'programming >= 4' : df[df['programming'] >= 4],
        'math >= 4 and programming >= 4' : df[(df['math'] >= 4) & (df['programming'] >= 4)],
        'math = 5 or programming = 5' : df[(df['math'] == 5) | (df['programming'] == 5)],
        'name of students with math >= 5' : (df[df['math'] >= 5 ])['name']
        }
#for key, value in task_3(df).items():
#    print(f'{key}: \n{value}\n')

#=================================Block 4=================================#

df["average"] = (df["math"] + df["programming"]) / 2
df['excellent'] = (df['average'] >= 4.5)

#print(df)

#=================================Block 5=================================#

def task_5(df):
    return{
       'df.sort_values("average")' : df.sort_values("average"),
       'df.sort_values("average", ascending=False)' : df.sort_values("average", ascending=False),
       'three students with the highest grade point average ' : (df.sort_values("average", ascending=False)).iloc[:3]  
    }

#for key, value in task_5(df).items():
#    print(f'{key}: \n{value}\n')


#=================================Block 6=================================#

df["gender"] = ["F", "M", "F", "M", "F"]

def task_6(df):
    return{
      'df.groupby("gender")["average"].mean()' : df.groupby("gender")["average"].mean(),
      'average math grade for each group' : df.groupby('gender')['math'].mean(),
      'max grade in programming' :  df.groupby('gender')['programming'].max(),
      'the number of students in each group ' : df.groupby('gender').size()
    }

#for key, value in task_6(df).items():
#    print(f'{key}: \n{value}\n')


#=================================Block 6=================================#

data = {
    "name": ["Anna", "Ivan", "Maria", "Petr", "Elena",
             "Alex", "Kate", "Max"],
    
    "age": [22, 23, 21, 24, 22, 25, 21, 23],
    
    "math": [5, 4, 5, 3, 5, 4, 5, 3],
    
    "programming": [4, 5, 4, 3, 4, 5, 5, 4],
    
    "hours_studied": [12, 8, 15, 5, 10, 14, 16, 7]
}

df = pd.DataFrame(data)

def menu(df):
    x = 1
    while x != 0:
        print('1. Who is the oldest?')
        print('2. Who studied for the most hours?')
        print('3. What is the average grade in mathematics?')
        print('4. What is the average grade in programming?')
        print('5. Create an \'average\'.')
        print('6. Who has an \'average\' >= 4.5?')
        print('7. Sort the students by \'hours_studied\'.')
        print('8. Is there a relationship between the number of study hours and the average grade?')
        print('0. Exit')
        print()
        x = int(input('Enter num from 0 to 8: '))
        print()

        if x == 0:
            return
        elif x == 1:
            print(f"{ df.loc[df['age'].idxmax(), 'name'] } is the oldest\n") #loc [row, col]
        elif x == 2:
            print(f"{ df.loc[df['hours_studied'].idxmax(), 'name'] } studied for the most hours\n")
        elif x == 3:
            print(f"average grade in mathematics: {df['math'].mean()}\n")
        elif x == 4:
            print(f"average grade in programming: {df['programming'].mean()}\n")
        elif x == 5:
            df['average'] = (df["math"] + df["programming"]) / 2
            print(f"average created:\n{df}\n")
        elif x == 6:
            if 'average' not in df.columns:
                print('You dont create average\n')
                continue
            print(f"average >= 4.5: \n{ df.loc[ (df['average'] >= 4.5), 'name'] }\n")
        elif x == 7:
            print(f"sorted by 'hours_studied': \n{df.sort_values( 'hours_studied', ascending = False) }\n")
        elif x == 8:
            if 'average' not in df.columns:
                print('You dont create average\n')
                continue
            print("I am listing each student's average score, sorted in descending order based on the total number of study hours.")
            df_sort =  df.sort_values('hours_studied', ascending = False)[['name', 'average', 'hours_studied']]
            print(df_sort)
            print('\nI am plotting a dependency graph.\n')
           
            plt.scatter(df['hours_studied'], df['average'])
            plt.title('dependency graph')
            plt.xlabel('hours studied')
            plt.ylabel('average')
            plt.grid(True)

            plt.show()



menu(df)