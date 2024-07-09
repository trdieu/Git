import pandas as pd
import matplotlib.pyplot as plt

# Step 2. Import the dataset
url = 'https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv'
titanic = pd.read_csv(url)

# Step 3. Assign it to a variable titanic
# (Already done above)

# Kiểm tra tên các cột
print(titanic.columns)

# Step 4. Set PassengerId as the index (Kiểm tra xem cột này có tồn tại không)
if 'PassengerId' in titanic.columns:
    titanic.set_index('PassengerId', inplace=True)
else:
    print("PassengerId column not found, setting a default index.")

# Step 5. Create a pie chart presenting the male/female proportion
gender_counts = titanic['Sex'].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140, colors=['skyblue', 'pink'])
plt.title('Male/Female Proportion')
plt.show()

# Step 6. Create a scatterplot with the Fare payed and the Age, differ the plot color by gender
colors = {'male': 'blue', 'female': 'red'}
plt.figure(figsize=(10, 6))
for gender in colors:
    subset = titanic[titanic['Sex'] == gender]
    plt.scatter(subset['Fare'], subset['Age'], c=colors[gender], label=gender, alpha=0.6)
plt.title('Fare vs Age by Gender')
plt.xlabel('Fare')
plt.ylabel('Age')
plt.legend()
plt.show()

# Step 7. How many people survived?
survived_count = titanic['Survived'].sum()
print(f'Number of people who survived: {survived_count}')

# Step 8. Create a histogram with the Fare payed
plt.figure(figsize=(10, 6))
plt.hist(titanic['Fare'], bins=30, edgecolor='k', alpha=0.7)
plt.title('Histogram of Fare')
plt.xlabel('Fare')
plt.ylabel('Frequency')
plt.show()

# BONUS: Create your own question and answer it.
# Question: What is the survival rate by class?
survival_rate_by_class = titanic.groupby('Pclass')['Survived'].mean()
plt.figure(figsize=(8, 6))
survival_rate_by_class.plot(kind='bar', color='lightgreen')
plt.title('Survival Rate by Class')
plt.xlabel('Class')
plt.ylabel('Survival Rate')
plt.show()
