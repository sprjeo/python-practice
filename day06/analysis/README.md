# Titanic Data Analysis

## About the project

This is a small exploratory data analysis of the Titanic dataset using **Python, Pandas, NumPy and Matplotlib**.

The goal was to explore the dataset, investigate missing values, analyze survival rates and visualize the main findings.

## Technologies

- Python
- Pandas
- NumPy
- Matplotlib

## Dataset

The analysis uses the Titanic dataset.

The dataset contains information about passengers, including:

- passenger class;
- sex;
- age;
- number of siblings/spouses aboard;
- number of parents/children aboard;
- ticket;
- fare;
- cabin;
- port of embarkation;
- survival status.

## Analysis

### Missing values

The largest percentage of missing values is found in the `Cabin` column — approximately **77%**. This makes the variable difficult to use for analysis without additional preprocessing.

The smallest number of missing values is found in `Embarked` — approximately **0.2%**.

The following columns contain no missing values:

`PassengerId`, `Survived`, `Pclass`, `Name`, `Sex`, `SibSp`, `Parch`, `Ticket`, `Fare`.

### Survival by sex

The survival rate was:

- **Women:** approximately 74.2%
- **Men:** approximately 18.9%

This shows a substantial difference in survival rates between men and women.

### Survival by passenger class

The survival rate by passenger class was:

- **1st class:** approximately 63.0%
- **2nd class:** approximately 47.3%
- **3rd class:** approximately 24.2%

The survival rate decreases as the passenger class becomes lower.

### Average age

The average age was:

- **Men:** approximately 30.7 years
- **Women:** approximately 27.9 years

### Survival by sex and passenger class

The highest survival rate was observed among **women in 1st class — approximately 96.8%**.

The lowest survival rate was observed among **men in 3rd class — approximately 13.5%**.

## Visualizations

The project includes visualizations showing:

1. Distribution of passengers by sex.
2. Survival distribution by sex.
3. Survival distribution by passenger class.

## Conclusions

1. The `Cabin` column contains the largest proportion of missing values (approximately 77%), making it difficult to use without additional preprocessing.
2. Women had a substantially higher survival rate than men: approximately 74.2% versus 18.9%.
3. Passengers in higher classes had higher survival rates: approximately 63.0% in 1st class, 47.3% in 2nd class and 24.2% in 3rd class.
4. The average age of male passengers was higher than that of female passengers.
5. The highest survival rate was observed among women in 1st class (approximately 96.8%), while the lowest was among men in 3rd class (approximately 13.5%).
6. Based on this analysis, **sex and passenger class are strongly associated with survival**, and their combination produces even more pronounced differences.



## Correlation analysis

### Findings

1. The correlation between *Pclass* and *Survived* has the largest absolute value (and is negative). The correlation is negative because a higher class corresponds to a higher survival rate. This implies that passengers in higher classes were more likely to survive; they likely enjoyed better living and dining conditions, and-crucially-their class status may have given them priority access to lifeboats during the emergency. This aligns with the results obtained using `groupby()`. Passengers in higher classes had higher survival rates. The analysis shows an association between passenger class and survival, but it does not establish causation.
2. The *Fare* < 100 was in high demand. More people aged 10 to 30 could afford a higher fare. The highest fares were paid by a couple of individuals aged 30–40.
3. Overall, survival rates show little dependence on age; however, the graph suggests that the majority of survivors are slightly younger than the majority of those who perished, even though the median age is higher for the survivors.
4. Among the survivors, there are many who paid a higher fare. However, the correlation here is not high.
5. The chart shows that the highest number of *SibSp* values ​​is found among people with 2 *Parch*. Next in terms of count is the group with 1 *Parch*, followed by 0, and then a descending order from 3 to 6.
6. Older passengers tended to be associated with higher passenger classes in this dataset.  
7. The higher the class, the higher the ticket price, accordingly.


## Visualizations

The project includes visualizations showing correlation between:
1. Age and fare
2. Age and survived
3. Fare and survived
4. Parch and sibsp
5. Age and pclass
6. Fare and pclass

### Important note

Correlation does not necessarily imply causation.

## Filtration analysis

### Findings

1. It is useful to create a DataFrame with only the columns you need when you do not need all the data for your analysis, or when some columns are missing most of the values.
2. After I limited the sample to adults, the survival rate changed. The difference between men and women widened even more, favoring women. The picture also changed across classes, with the survival rate for the second and third classes falling by 6 and 4 percent, respectively.

## What I practiced

During this project I practiced:

- loading CSV data with `pandas.read_csv()`;
- exploring a DataFrame;
- working with missing values;
- filtering data;
- using `groupby()`, `corr()`, `loc[]`;
- calculating averages and proportions;
- working with multiple grouping variables;
- creating visualizations with Matplotlib;
- interpreting analytical results.


