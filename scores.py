#Scores
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Import necessary libraries (already imported)

# Step 2: Create the DataFrame
data = {
    'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
    'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
    'age': [42, 52, 36, 24, 73],
    'female': [0, 1, 1, 0, 1],
    'preTestScore': [4, 24, 31, 2, 3],
    'postTestScore': [25, 94, 57, 62, 70]
}

df = pd.DataFrame(data)
print("DataFrame:")
print(df)
print()

# Step 3: Create a Scatterplot of preTestScore and postTestScore, with the size of each point determined by age
plt.scatter(df['preTestScore'], df['postTestScore'], s=df['age'], alpha=0.5)
plt.xlabel('preTestScore')
plt.ylabel('postTestScore')
plt.title('Scatterplot of preTestScore vs postTestScore (Size by Age)')
plt.show()

# Step 4: Create a Scatterplot of preTestScore and postTestScore, with size 4.5 times postTestScore and color by sex
sizes = 4.5 * df['postTestScore']  # Size is 4.5 times postTestScore
colors = df['female']             # Color is determined by female (0: male, 1: female)

plt.scatter(df['preTestScore'], df['postTestScore'], s=sizes, c=colors, alpha=0.5, cmap='viridis')
plt.xlabel('preTestScore')
plt.ylabel('postTestScore')
plt.title('Scatterplot of preTestScore vs postTestScore (Size and Color by Sex)')
plt.colorbar(label='Female (0: Male, 1: Female)')
plt.show()

# BONUS: Create your own question and answer it

# Question: Is there a relationship between preTestScore and postTestScore when considering age?

# Answer: To answer this question, we can explore the data visually with a scatterplot.

plt.scatter(df['preTestScore'], df['postTestScore'], c=df['age'], cmap='coolwarm', alpha=0.8)
plt.xlabel('preTestScore')
plt.ylabel('postTestScore')
plt.title('Scatterplot of preTestScore vs postTestScore (Color by Age)')
plt.colorbar(label='Age')
plt.show()