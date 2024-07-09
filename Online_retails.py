import pandas as pd
import matplotlib.pyplot as plt

# Step 2. Import the dataset
url = 'your_dataset_url_here'
online_rt = pd.read_csv(url, encoding='latin1')

# Step 3. Assign it to a variable called online_rt
# (Already done above)

# Step 4. Create a histogram with the 10 countries that have the most 'Quantity' ordered except UK
country_quantity = online_rt[online_rt['Country'] != 'United Kingdom'].groupby('Country')['Quantity'].sum()
top_10_countries = country_quantity.nlargest(10)

plt.figure(figsize=(10, 6))
top_10_countries.plot(kind='bar')
plt.title('Top 10 Countries by Quantity Ordered (excluding UK)')
plt.xlabel('Country')
plt.ylabel('Total Quantity Ordered')
plt.show()

# Step 5. Exclude negative Quantity entries
online_rt = online_rt[online_rt['Quantity'] > 0]

# Step 6. Create a scatterplot with the Quantity per UnitPrice by CustomerID for the top 3 Countries (except UK)
top_countries = online_rt[online_rt['Country'] != 'United Kingdom'].groupby('Country')['Quantity'].sum().nlargest(3).index

for country in top_countries:
    country_data = online_rt[online_rt['Country'] == country]
    plt.figure(figsize=(10, 6))
    for customer_id in country_data['CustomerID'].unique():
        customer_data = country_data[country_data['CustomerID'] == customer_id]
        plt.scatter(customer_data['UnitPrice'], customer_data['Quantity'], label=str(customer_id), alpha=0.5)
    plt.title(f'Quantity per UnitPrice by CustomerID in {country}')
    plt.xlabel('UnitPrice')
    plt.ylabel('Quantity')
    plt.show()

# Step 7. Investigate why the previous results look so uninformative
print(online_rt.head())
print(online_rt['UnitPrice'].dtype)

customer_data = online_rt[online_rt['CustomerID'].isin([12346.0, 12347.0])]
print(customer_data)

# Step 7.2.1 Find out the top 3 countries in terms of sales volume
top_countries_by_volume = online_rt[online_rt['Country'] != 'United Kingdom'].groupby('Country')['Quantity'].sum().nlargest(3).index
print(top_countries_by_volume)

# Step 7.2.2 Group by CustomerID and Country and find out the average price (AvgPrice) each customer spends per unit
online_rt['Revenue'] = online_rt['Quantity'] * online_rt['UnitPrice']

customer_avg_price = online_rt.groupby(['CustomerID', 'Country']).agg({'Revenue': 'sum', 'Quantity': 'sum'})
customer_avg_price['AvgPrice'] = customer_avg_price['Revenue'] / customer_avg_price['Quantity']
customer_avg_price = customer_avg_price.reset_index()
customer_avg_price_top = customer_avg_price[customer_avg_price['Country'].isin(top_countries_by_volume)]

for country in top_countries_by_volume:
    country_data = customer_avg_price_top[customer_avg_price_top['Country'] == country]
    plt.figure(figsize=(10, 6))
    plt.scatter(country_data['AvgPrice'], country_data['Quantity'], alpha=0.5)
    plt.title(f'Quantity per AvgPrice by CustomerID in {country}')
    plt.xlabel('AvgPrice')
    plt.ylabel('Total Quantity')
    plt.show()

# Step 7.4 Plot the data regardless of Country
plt.figure(figsize=(10, 6))
plt.scatter(customer_avg_price['AvgPrice'], customer_avg_price['Quantity'], alpha=0.5)
plt.title('Quantity per AvgPrice by CustomerID (All Countries)')
plt.xlabel('AvgPrice')
plt.ylabel('Total Quantity')
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(customer_avg_price['AvgPrice'], customer_avg_price['Quantity'], alpha=0.5)
plt.xlim(0, 100)
plt.ylim(0, 1000)
plt.title('Quantity per AvgPrice by CustomerID (Zoomed In)')
plt.xlabel('AvgPrice')
plt.ylabel('Total Quantity')
plt.show()

# Step 8. Plot a line chart showing revenue (y) per UnitPrice (x)
price_intervals = pd.cut(online_rt['UnitPrice'], bins=range(0, 51))
grouped = online_rt.groupby(price_intervals).agg({'Revenue': 'sum', 'Quantity': 'sum'})

plt.figure(figsize=(10, 6))
plt.plot(grouped.index.astype(str), grouped['Revenue'], marker='o')
plt.title('Revenue per UnitPrice')
plt.xlabel('UnitPrice Intervals')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.show()

# BONUS: Create your own question and answer it.
for country in top_countries_by_volume:
    country_data = online_rt[online_rt['Country'] == country]
    top_item = country_data.groupby('Description')['Quantity'].sum().idxmax()
    print(f'Top item in {country}: {top_item}')
