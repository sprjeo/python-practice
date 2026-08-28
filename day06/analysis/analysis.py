import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(url)

#print(df.head())
#print(df.shape)
#print(df.columns)
#print(df.dtypes)
#print(df.describe())
#print(df.info())

#print(df.isna().sum())
#print(df.isna().mean() * 100)

def analyze_data(df):
    return{
        'the largest amount of gaps' :df.isna().sum().idxmax(),
        'the percentage of gaps is' : ((df.isna().mean()*100).max()),
        'column with minimal gaps' : df.isna().sum()[df.isna().sum() > 0].idxmin(),
        'Percentage of survivors' : df["Survived"].mean(),
        'Survivors of each sex' : df.groupby('Sex')['Survived'].mean(),
        'Number of first-class survivors' : df[df['Pclass'] == 1].groupby('Survived')['Pclass'].count(),
        'Number of second-class survivors' : df[df['Pclass'] == 2].groupby('Survived')['Pclass'].count(),
        'Number of third-class survivors' : df[df['Pclass'] == 3].groupby('Survived')['Pclass'].count(),
        'Percentage of survivors of each class' : df.groupby('Pclass')['Survived'].mean() * 100,
        'Average age of each sex' : df.groupby('Sex')['Age'].mean(),
        'Number of survivors by class and sex' : df.groupby(['Sex', 'Pclass'])['Survived'].mean()
        }


#for key, value in analyze_data(df).items():
#    print(f'{key}: \n{value}\n')


def visualization(df):
    sex_counts = df['Sex'].value_counts()

    plt.bar(sex_counts.index, sex_counts.values, color =['blue', 'red'])
    plt.title('Distribution of passengers by gender')
    plt.ylabel('Number of people')
    plt.show()

    surv_sex_count = df.groupby('Sex')['Survived'].value_counts() #made list: ['female, 1',...., 'male, 0']
    x_labels = [f'{sex}, {surv}' for sex, surv in surv_sex_count.index]
    plt.bar(x_labels, surv_sex_count.values, color=['green', 'red', 'red', 'green'])
    plt.title('Survival rates of men and women')
    plt.ylabel('Number of people')
    plt.show()

    class_surv = df.groupby('Pclass')['Survived'].value_counts()
    x_labels = [f'{pclass}, {surv}' for pclass, surv in class_surv.index]
    plt.bar(x_labels, class_surv.values, color = ['green', 'red', 'red', 'green', 'red', 'green']) 
    plt.title('Survival rate based on ticket class')
    plt.show()


visualization(df)
    

