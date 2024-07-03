#EX1
# Bước 1: Import các thư viện cần thiết
import pandas as pd

# Bước 2: Tải dữ liệu từ địa chỉ
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00320/student.zip'
df = pd.read_csv(url, sep=';')

# Bước 3: Gán dữ liệu vào biến df
# (đã thực hiện ở bước 2)

# Bước 4: Cắt dữ liệu từ cột 'school' đến cột 'guardian'
df = df.loc[:, 'school':'guardian']

# Bước 5: Tạo hàm lambda để viết hoa chuỗi
capitalize = lambda x: x.capitalize()

# Bước 6: Viết hoa cột Mjob và Fjob
df['Mjob'] = df['Mjob'].apply(capitalize)
df['Fjob'] = df['Fjob'].apply(capitalize)

# Bước 7: In các phần tử cuối cùng của dữ liệu
print(df.tail())

# Bước 8: Ghi đè dữ liệu viết hoa vào dataframe gốc
df['Mjob'] = df['Mjob'].str.capitalize()
df['Fjob'] = df['Fjob'].str.capitalize()
print(df.tail())

# Bước 9: Tạo hàm majority và thêm cột legal_drinker
def majority(age):
    return age > 17

df['legal_drinker'] = df['age'].apply(majority)

# Bước 10: Nhân mỗi số trong dữ liệu với 10
df_multiplied = df.select_dtypes(include=['int64', 'float64']) * 10
df.update(df_multiplied)

print(df.head())

#EX2
# Bước 1: Import các thư viện cần thiết
import pandas as pd

# Bước 2: Tải dữ liệu từ địa chỉ mới
url = 'https://github.com/justmarkham/DAT8/blob/master/data/u.s._crime_rates_1960_2014.csv?raw=true'
crime = pd.read_csv(url)

# Bước 3: Gán dữ liệu vào biến crime
# (đã thực hiện ở bước 2)

# Bước 4: Kiểm tra kiểu dữ liệu của các cột
print(crime.dtypes)

# Bước 5: Chuyển đổi kiểu dữ liệu của cột Year thành datetime64
crime['Year'] = pd.to_datetime(crime['Year'], format='%Y')

# Bước 6: Đặt cột Year làm chỉ mục của dataframe
crime.set_index('Year', inplace=True)

# Bước 7: Xóa cột Total
crime.drop(columns='Total', inplace=True)

# Bước 8: Nhóm dữ liệu theo thập kỷ và tính tổng các giá trị
crime['Decade'] = (crime.index.year // 10) * 10
decade_crime = crime.groupby('Decade').sum()
decade_crime['Population'] = crime.groupby('Decade')['Population'].mean()

# Bước 9: Tìm thập kỷ nguy hiểm nhất để sống ở Mỹ
most_dangerous_decade = decade_crime.drop(columns='Population').sum(axis=1).idxmax()
print(f"Thập kỷ nguy hiểm nhất để sống ở Mỹ: {most_dangerous_decade}")

# In kết quả
print(decade_crime)
