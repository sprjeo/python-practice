import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(url)


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

   

#correlation


def visual_corr(df):
    print(df.corr(numeric_only=True))

    plt.scatter(df['Age'], df['Fare'])
    plt.title('correlation between age and fare')
    plt.xlabel('age')
    plt.ylabel('fare')
    plt.show()

    plt.scatter(df['Age'], df['Survived'])
    plt.title('correlation between age and survived')
    plt.xlabel('age')
    plt.ylabel('survived')
    plt.show()

    df.boxplot(column="Age", by="Survived")
    plt.show()

    plt.scatter(df['Fare'], df['Survived'])
    plt.title('correlation between fare and survived')
    plt.xlabel('fare')
    plt.ylabel('survived')
    plt.show()

    plt.scatter(df['Parch'], df['SibSp'])
    plt.title('correlation between parch and sibsp')
    plt.xlabel('parch')
    plt.ylabel('sibsp')
    plt.show()

    df.boxplot(column="Age", by="Pclass")
    plt.show()

    df.boxplot(column="Fare", by="Pclass")
    plt.show()



#What to do with missing data

df_drop = df.dropna(subset=["Age"])

# A: dropna. Remove passengers with unknown ages. 
# advantages: Accurate analyses when working with age.
# disadvantages: This removes some potentially important data during analysis

df_fill = df.copy()
df_fill["Age"] = df_fill["Age"].fillna(df_fill["Age"].median())

# B: fillna. Fill unknown ages with the median.
# advantages: This leaves the data for analysis
# disadvantages: Age-related analyses may be performed incorrectly



#Working with columns


passengers = df[["Sex", "Age", "Pclass", "Fare", "Survived"]].copy()


#Filtration

def filtration(df):
    return{
        'Surviving passengers over 70 and under 20' : df[((df['Age'] > 70) | (df['Age'] < 20)) & (df['Survived'] == 1)],
        'First-class passengers under 18' : df[(df['Age'] < 18) & (df['Pclass'] == 1)],
        'Single women in first class' : df[(df['SibSp'] == 0) & (df['Parch'] == 0) & (df['Pclass'] == 1)],
        'Third-class survivors' : df[(df['Pclass'] == 3) & (df['Survived'] == 1)],
        'Men with fare more than 100' : df[(df['Sex'] == 'male') & (df['Fare'] > 100)]
        }


#print(df.loc[df['Sex'] == 'male', ['Age', 'Fare', 'Survived']])

adult_passengers = df.copy()
adult_passengers = adult_passengers.loc[
                    adult_passengers['Age'] >= 18,
                    ['Sex', 'Age', 'Pclass', 'Fare', 'Survived']]

def surv_rate(df):
    return{
       'Survival rate of males and females among adults' : df.groupby('Sex')['Survived'].mean(),
       'Survival rate for each adult class' : df.groupby('Pclass')['Survived'].mean()
        }


