#folder 02
import pandas as pd
import numpy as np

#ex1

# Bước 2: Nhập dữ liệu từ địa chỉ này
url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"
chipo = pd.read_csv(url, sep='\t')

# Bước 4: Có bao nhiêu sản phẩm có giá trên $10.00
chipo['item_price'] = chipo['item_price'].apply(lambda x: float(x[1:]))
products_above_10 = chipo[chipo['item_price'] > 10.00]['item_name'].nunique()
print(f"Số lượng sản phẩm có giá trên $10.00: {products_above_10}")

# Bước 5: Giá của mỗi mặt hàng là bao nhiêu
item_prices = chipo[['item_name', 'item_price']].drop_duplicates()
print(item_prices)

# Bước 6: Sắp xếp theo tên của mặt hàng
sorted_items = item_prices.sort_values(by='item_name')
print(sorted_items)

# Bước 7: Số lượng của mặt hàng đắt nhất đã được đặt
most_expensive_item = chipo.sort_values(by='item_price', ascending=False).iloc[0]
most_expensive_item_quantity = most_expensive_item['quantity']
print(f"Số lượng của mặt hàng đắt nhất đã được đặt: {most_expensive_item_quantity}")

# Bước 8: Bao nhiêu lần một món Veggie Salad Bowl đã được đặt
veggie_salad_bowl_orders = chipo[chipo['item_name'] == 'Veggie Salad Bowl'].shape[0]
print(f"Số lần món Veggie Salad Bowl đã được đặt: {veggie_salad_bowl_orders}")

# Bước 9: Bao nhiêu lần có người đặt hơn một Canned Soda
canned_soda_orders = chipo[(chipo['item_name'] == 'Canned Soda') & (chipo['quantity'] > 1)].shape[0]
print(f"Số lần có người đặt hơn một Canned Soda: {canned_soda_orders}")

#ex2
# Step 1: Import the necessary libraries
import pandas as pd

# Step 2: Import the dataset from the address
url = 'https://raw.githubusercontent.com/datasets/euro-2012/master/data/euro12.csv'
euro12 = pd.read_csv(url)

# Step 3: Assign it to a variable called euro12
# (already done above)

# Step 4: Select only the Goal column
goals = euro12['Goals']

# Step 5: How many teams participated in the Euro2012?
num_teams = euro12.shape[0]

# Step 6: What is the number of columns in the dataset?
num_columns = euro12.shape[1]

# Step 7: View only the columns Team, Yellow Cards, and Red Cards and assign them to a dataframe called discipline
discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]

# Step 8: Sort the teams by Red Cards, then by Yellow Cards
sorted_discipline = discipline.sort_values(by=['Red Cards', 'Yellow Cards'], ascending=[False, False])

# Step 9: Calculate the mean Yellow Cards given per Team
mean_yellow_cards = euro12['Yellow Cards'].mean()

# Step 10: Filter teams that scored more than 6 goals
teams_more_than_6_goals = euro12[euro12['Goals'] > 6]

# Step 11: Select the teams that start with G
teams_start_with_g = euro12[euro12['Team'].str.startswith('G')]

# Step 12: Select the first 7 columns
first_7_columns = euro12.iloc[:, :7]

# Step 13: Select all columns except the last 3
all_except_last_3 = euro12.iloc[:, :-3]

# Step 14: Present only the Shooting Accuracy from England, Italy, and Russia
shooting_accuracy_selected_teams = euro12[euro12['Team'].isin(['England', 'Italy', 'Russia'])][['Team', 'Shooting Accuracy']]

# Output results for verification
print("Goals Column:\n", goals.head(), "\n")
print("Number of Teams:", num_teams, "\n")
print("Number of Columns:", num_columns, "\n")
print("Discipline DataFrame:\n", discipline.head(), "\n")
print("Sorted Discipline DataFrame:\n", sorted_discipline.head(), "\n")
print("Mean Yellow Cards per Team:", mean_yellow_cards, "\n")
print("Teams with more than 6 goals:\n", teams_more_than_6_goals[['Team', 'Goals']], "\n")
print("Teams that start with G:\n", teams_start_with_g[['Team']], "\n")
print("First 7 Columns:\n", first_7_columns.head(), "\n")
print("All Columns except the last 3:\n", all_except_last_3.head(), "\n")
print("Shooting Accuracy for England, Italy, and Russia:\n", shooting_accuracy_selected_teams, "\n")
