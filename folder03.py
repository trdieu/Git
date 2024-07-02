import pandas as pd
import numpy as np

#US_Baby_Names
# Bước 1: Import bộ dữ liệu từ địa chỉ
url = 'https://raw.githubusercontent.com/openai-code/datasets/main/us_baby_names_2004-2014.csv'
baby_names = pd.read_csv(url)

# Bước 2: Gán nó vào biến có tên là baby_names
# (đã làm ở trên)

# Bước 3: Xem 10 mục đầu tiên
first_10_entries = baby_names.head(10)
print("10 mục đầu tiên:\n", first_10_entries, "\n")

# Bước 4: Xóa cột 'Unnamed: 0' và 'Id'
baby_names.drop(columns=['Unnamed: 0', 'Id'], inplace=True)

# Bước 5: Có nhiều tên nam hay nữ hơn trong bộ dữ liệu?
gender_counts = baby_names['Gender'].value_counts()
print("Số lượng tên theo giới tính:\n", gender_counts, "\n")

# Bước 6: Nhóm bộ dữ liệu theo tên và gán vào biến names
names_grouped = baby_names.groupby('Name').sum()

# Bước 7: Có bao nhiêu tên khác nhau trong bộ dữ liệu?
num_unique_names = names_grouped.shape[0]
print("Số lượng tên khác nhau:", num_unique_names, "\n")

# Bước 8: Tên nào có số lần xuất hiện nhiều nhất?
most_occurrences_name = names_grouped['Count'].idxmax()
most_occurrences_count = names_grouped['Count'].max()
print("Tên có số lần xuất hiện nhiều nhất:", most_occurrences_name, "với số lượng:", most_occurrences_count, "\n")

# Bước 9: Có bao nhiêu tên khác nhau có số lần xuất hiện ít nhất?
least_occurrences_count = names_grouped['Count'].min()
num_least_occurrences = (names_grouped['Count'] == least_occurrences_count).sum()
print("Số lượng tên khác nhau có số lần xuất hiện ít nhất:", num_least_occurrences, "\n")

# Bước 10: Số lần xuất hiện trung bình của tên là bao nhiêu?
median_name_occurrence = names_grouped['Count'].median()
print("Số lần xuất hiện trung bình của tên:", median_name_occurrence, "\n")

# Bước 11: Độ lệch chuẩn của số lần xuất hiện của tên là bao nhiêu?
std_name_occurrence = names_grouped['Count'].std()
print("Độ lệch chuẩn của số lần xuất hiện của tên:", std_name_occurrence, "\n")

# Bước 12: Nhận một bản tóm tắt với trung bình, min, max, std và các phần tư
summary_statistics = names_grouped['Count'].describe()
print("Thống kê tóm tắt:\n", summary_statistics, "\n")

#Wind_stats
# Bước 1: Import các thư viện cần thiết
import pandas as pd
import numpy as np

# Bước 2: Import bộ dữ liệu từ địa chỉ
url = 'https://raw.githubusercontent.com/openai-code/datasets/main/wind.data'
data = pd.read_csv(url, delim_whitespace=True)

# Bước 3: Gán nó vào biến có tên là data và thay thế 3 cột đầu bằng một chỉ mục datetime thích hợp
data['Yr'] = data['Yr'].apply(lambda x: x + 1900)
data['date'] = pd.to_datetime(data[['Yr', 'Mo', 'Dy']])
data = data.set_index('date')
data = data.drop(columns=['Yr', 'Mo', 'Dy'])

# Bước 4: Tạo hàm để sửa năm 2061 thành 1961 và áp dụng nó
def fix_year(x):
    year = x.year - 100 if x.year > 1999 else x.year
    return pd.Timestamp(year=year, month=x.month, day=x.day)

data.index = data.index.map(fix_year)

# Bước 5: Đặt đúng chỉ mục là ngày tháng. Chú ý kiểu dữ liệu nên là datetime64[ns]
data.index = pd.to_datetime(data.index)

# Bước 6: Tính xem có bao nhiêu giá trị bị thiếu cho mỗi địa điểm trong toàn bộ bản ghi
missing_values_per_location = data.isnull().sum()

# Bước 7: Tính tổng số giá trị không bị thiếu
total_non_missing_values = data.notnull().sum().sum()

# Bước 8: Tính tốc độ gió trung bình của tất cả các địa điểm và thời gian
mean_windspeed = data.mean().mean()

# Bước 9: Tạo DataFrame có tên loc_stats và tính toán min, max, mean và độ lệch chuẩn của tốc độ gió tại mỗi địa điểm
loc_stats = data.describe().loc[['min', 'max', 'mean', 'std']].T

# Bước 10: Tạo DataFrame có tên day_stats và tính toán min, max, mean và độ lệch chuẩn của tốc độ gió qua tất cả các địa điểm tại mỗi ngày
day_stats = data.T.describe().loc[['min', 'max', 'mean', 'std']].T

# Bước 11: Tìm tốc độ gió trung bình trong tháng 1 cho mỗi địa điểm
january_windspeed = data[data.index.month == 1].mean()

# Bước 12: Downsample bản ghi xuống tần suất hàng năm cho mỗi địa điểm
yearly_windspeed = data.resample('Y').mean()

# Bước 13: Downsample bản ghi xuống tần suất hàng tháng cho mỗi địa điểm
monthly_windspeed = data.resample('M').mean()

# Bước 14: Downsample bản ghi xuống tần suất hàng tuần cho mỗi địa điểm
weekly_windspeed = data.resample('W').mean()

# Bước 15: Tính min, max, mean và độ lệch chuẩn của tốc độ gió qua tất cả các địa điểm cho mỗi tuần trong 52 tuần đầu tiên
weekly_stats = weekly_windspeed[:52].describe().loc[['min', 'max', 'mean', 'std']].T

# Xuất kết quả để kiểm tra
print("Missing values per location:\n", missing_values_per_location, "\n")
print("Total non-missing values:", total_non_missing_values, "\n")
print("Mean windspeed over all locations and times:", mean_windspeed, "\n")
print("Location stats:\n", loc_stats, "\n")
print("Day stats:\n", day_stats, "\n")
print("Average windspeed in January for each location:\n", january_windspeed, "\n")
print("Yearly windspeed:\n", yearly_windspeed.head(), "\n")
print("Monthly windspeed:\n", monthly_windspeed.head(), "\n")
print("Weekly windspeed:\n", weekly_windspeed.head(), "\n")
print("Weekly stats for the first 52 weeks:\n", weekly_stats, "\n")
