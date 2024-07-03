#EX1
# Bước 1: Import các thư viện cần thiết
import pandas as pd
import numpy as np

# Bước 2: Tải dữ liệu từ địa chỉ
url1 = 'https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'
url2 = 'https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'

# Bước 3: Gán dữ liệu vào biến cars1 và cars2
cars1 = pd.read_csv(url1, header=None)
cars2 = pd.read_csv(url2, header=None)

# Bước 4: Sửa lỗi các cột trống không tên trong cars1
cars1 = cars1.dropna(axis=1, how='all')

# Bước 5: Đếm số quan sát trong mỗi dataset
print(f"Số lượng quan sát trong cars1: {cars1.shape[0]}")
print(f"Số lượng quan sát trong cars2: {cars2.shape[0]}")

# Bước 6: Nối cars1 và cars2 thành một DataFrame gọi là cars
cars = pd.concat([cars1, cars2], ignore_index=True)

# Bước 7: Tạo cột owners với số ngẫu nhiên từ 15,000 đến 73,000
np.random.seed(0)  # Để đảm bảo kết quả ngẫu nhiên có thể tái lập
owners = np.random.randint(15000, 73001, size=cars.shape[0])

# Bước 8: Thêm cột owners vào cars
cars['owners'] = owners

# In kết quả
print(cars.head())

#EX2
# Bước 1: Import các thư viện cần thiết
import pandas as pd

# Bước 2: Tạo 3 DataFrame dựa trên dữ liệu thô
raw_data_1 = {
    'subject_id': ['1', '2', '3', '4', '5'],
    'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
    'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']
}

raw_data_2 = {
    'subject_id': ['4', '5', '6', '7', '8'],
    'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
    'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']
}

raw_data_3 = {
    'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
    'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]
}

# Bước 3: Gán dữ liệu vào biến data1, data2, data3
data1 = pd.DataFrame(raw_data_1)
data2 = pd.DataFrame(raw_data_2)
data3 = pd.DataFrame(raw_data_3)

# Bước 4: Nối hai dataframe theo hàng và gán vào biến all_data
all_data = pd.concat([data1, data2], ignore_index=True)

# Bước 5: Nối hai dataframe theo cột và gán vào biến all_data_col
all_data_col = pd.concat([data1, data2], axis=1)

# Bước 6: In data3
print(data3)

# Bước 7: Gộp all_data và data3 theo giá trị subject_id
merged_data = pd.merge(all_data, data3, on='subject_id', how='inner')

# Bước 8: Gộp chỉ dữ liệu có cùng subject_id trong cả data1 và data2
merged_same_subject_id = pd.merge(data1, data2, on='subject_id', how='inner')

# Bước 9: Gộp tất cả các giá trị trong data1 và data2, với các bản ghi khớp từ cả hai bên
merged_all_values = pd.merge(data1, data2, on='subject_id', how='outer')

# In kết quả
print("All Data:")
print(all_data)
print("\nAll Data Columns:")
print(all_data_col)
print("\nMerged Data (all_data & data3):")
print(merged_data)
print("\nMerged Same Subject ID (data1 & data2):")
print(merged_same_subject_id)
print("\nMerged All Values (data1 & data2):")
print(merged_all_values)


#EX3
# Bước 1: Import các thư viện cần thiết
import pandas as pd
import numpy as np

# Bước 2: Tạo 3 Series khác nhau, mỗi Series có độ dài 100
np.random.seed(0)  # Để đảm bảo kết quả ngẫu nhiên có thể tái lập
series1 = pd.Series(np.random.randint(1, 5, size=100))
series2 = pd.Series(np.random.randint(1, 4, size=100))
series3 = pd.Series(np.random.randint(10000, 30001, size=100))

# Bước 3: Tạo DataFrame bằng cách nối các Series theo cột
df = pd.concat([series1, series2, series3], axis=1)

# Bước 4: Đổi tên các cột thành bedrs, bathrs, price_sqr_meter
df.columns = ['bedrs', 'bathrs', 'price_sqr_meter']

# Bước 5: Tạo một DataFrame có một cột với các giá trị của 3 Series và gán vào 'bigcolumn'
bigcolumn = pd.concat([series1, series2, series3], axis=0).to_frame(name='bigcolumn')

# Bước 6: Kiểm tra xem DataFrame chỉ có đến index 99
print(bigcolumn.index)

# Bước 7: Đánh lại chỉ mục của DataFrame để nó đi từ 0 đến 299
bigcolumn.reset_index(drop=True, inplace=True)

# In kết quả
print("DataFrame with renamed columns:")
print(df.head())
print("\nOne column DataFrame with values of the 3 Series:")
print(bigcolumn.head(105))  # In 105 dòng đầu tiên để kiểm tra

# Kiểm tra chỉ mục sau khi đánh lại
print("\nIndex after reindexing:")
print(bigcolumn.index)
