import pandas as pd

df = pd.read_csv('50_Startups.csv')

print("5 dòng đầu:")
print(df.head())

print("\nThông tin tổng quan:")
print(df.info())


print("\nThống kê mô tả:")
print(df.describe())


df['Total_Spend'] = df['R&D Spend'] + df['Administration'] + df['Marketing Spend']
print("\nTổng chi phí và lợi nhuận:")
print(df[['Total_Spend', 'Profit']].head())

print("\nLợi nhuận trung bình theo bang:")
print(df.groupby('State')['Profit'].mean())

print("\nBang có lợi nhuận cao nhất:")
max_profit_state = df.groupby('State')['Profit'].mean().idxmax()
print(f"→ {max_profit_state}")

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='Total_Spend', y='Profit', hue='State')
plt.title('Tổng Chi Phí vs Lợi Nhuận')
plt.xlabel('Tổng Chi Phí')
plt.ylabel('Lợi Nhuận')
plt.show()
