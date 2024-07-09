import pandas as pd
import matplotlib.pyplot as plt

# Step 2. Import the dataset
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
tips = pd.read_csv(url)

# Step 3. Assign it to a variable called tips
# (Already done above)

# Step 4. Delete the Unnamed 0 column
if 'Unnamed: 0' in tips.columns:
    tips = tips.drop(columns=['Unnamed: 0'])

# Step 5. Plot the total_bill column histogram
plt.figure(figsize=(8, 6))
plt.hist(tips['total_bill'], bins=30, edgecolor='k', alpha=0.7)
plt.title('Total Bill Histogram')
plt.xlabel('Total Bill')
plt.ylabel('Frequency')
plt.show()

# Step 6. Create a scatter plot presenting the relationship between total_bill and tip
plt.figure(figsize=(8, 6))
plt.scatter(tips['total_bill'], tips['tip'], alpha=0.7)
plt.title('Total Bill vs Tip')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.show()

# Step 7. Create one image with the relationship of total_bill, tip and size
plt.figure(figsize=(8, 6))
plt.scatter(tips['total_bill'], tips['tip'], s=tips['size']*20, alpha=0.7)  # size is proportional to the 'size' column
plt.title('Total Bill vs Tip (Size as bubble size)')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.show()

# Step 8. Present the relationship between days and total_bill value
plt.figure(figsize=(8, 6))
tips.groupby('day')['total_bill'].sum().plot(kind='bar', color='skyblue')
plt.title('Total Bill per Day')
plt.xlabel('Day')
plt.ylabel('Total Bill')
plt.show()

# Step 9. Create a scatter plot with the day as the y-axis and tip as the x-axis, differ the dots by sex
plt.figure(figsize=(8, 6))
for sex in tips['sex'].unique():
    subset = tips[tips['sex'] == sex]
    plt.scatter(subset['tip'], subset['day'], label=sex, alpha=0.7)
plt.title('Tip vs Day (differentiated by Sex)')
plt.xlabel('Tip')
plt.ylabel('Day')
plt.legend()
plt.show()

# Step 10. Create a box plot presenting the total_bill per day differentiating the time (Dinner or Lunch)
plt.figure(figsize=(8, 6))
tips.boxplot(column='total_bill', by=['day', 'time'], grid=False)
plt.title('Total Bill per Day and Time')
plt.suptitle('')
plt.xlabel('Day, Time')
plt.ylabel('Total Bill')
plt.show()

# Step 11. Create two histograms of the tip value based for Dinner and Lunch. They must be side by side.
fig, axs = plt.subplots(1, 2, figsize=(14, 6), sharey=True)
tips[tips['time'] == 'Dinner']['tip'].plot(kind='hist', bins=20, edgecolor='k', alpha=0.7, ax=axs[0])
tips[tips['time'] == 'Lunch']['tip'].plot(kind='hist', bins=20, edgecolor='k', alpha=0.7, ax=axs[1])

axs[0].set_title('Tip Value (Dinner)')
axs[0].set_xlabel('Tip')
axs[0].set_ylabel('Frequency')

axs[1].set_title('Tip Value (Lunch)')
axs[1].set_xlabel('Tip')

plt.show()

# Step 12. Create two scatterplots graphs, one for Male and another for Female, presenting the total_bill value and tip relationship, differing by smoker or no smoker
fig, axs = plt.subplots(1, 2, figsize=(14, 6), sharey=True, sharex=True)
for smoker_status in tips['smoker'].unique():
    male_subset = tips[(tips['sex'] == 'Male') & (tips['smoker'] == smoker_status)]
    female_subset = tips[(tips['sex'] == 'Female') & (tips['smoker'] == smoker_status)]
    axs[0].scatter(male_subset['total_bill'], male_subset['tip'], label=f'Smoker: {smoker_status}', alpha=0.7)
    axs[1].scatter(female_subset['total_bill'], female_subset['tip'], label=f'Smoker: {smoker_status}', alpha=0.7)

axs[0].set_title('Total Bill vs Tip (Male)')
axs[0].set_xlabel('Total Bill')
axs[0].set_ylabel('Tip')
axs[0].legend()

axs[1].set_title('Total Bill vs Tip (Female)')
axs[1].set_xlabel('Total Bill')
axs[1].legend()

plt.show()

# BONUS: Create your own question and answer it using a graph.
# Question: How does the average tip amount vary by day and time?
avg_tip = tips.groupby(['day', 'time'])['tip'].mean().unstack()

avg_tip.plot(kind='bar', figsize=(10, 6))
plt.title('Average Tip Amount by Day and Time')
plt.xlabel('Day')
plt.ylabel('Average Tip')
plt.show()
