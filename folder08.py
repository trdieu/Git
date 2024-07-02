#Iris
# Bước 1: Import các thư viện cần thiết
import pandas as pd
import numpy as np

# Bước 2: Import bộ dữ liệu từ địa chỉ
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
iris = pd.read_csv(url)

# Bước 3: Gán nó vào biến có tên là iris
# (đã làm ở trên)

# Bước 4: Tạo các cột cho bộ dữ liệu
iris.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

# Bước 5: Có giá trị nào bị thiếu trong dataframe không?
missing_values = iris.isnull().sum()
print("Có giá trị nào bị thiếu không?\n", missing_values, "\n")

# Bước 6: Đặt giá trị của các hàng từ 10 đến 29 của cột 'petal_length' thành NaN
iris.loc[10:29, 'petal_length'] = np.nan

# Bước 7: Thay thế các giá trị NaN bằng 1.0
iris['petal_length'].fillna(1.0, inplace=True)

# Bước 8: Xóa cột class
iris.drop(columns=['class'], inplace=True)

# Bước 9: Đặt 3 hàng đầu tiên thành NaN
iris.iloc[0:3] = np.nan

# Bước 10: Xóa các hàng có giá trị NaN
iris.dropna(inplace=True)

# Bước 11: Reset chỉ mục để bắt đầu lại từ 0
iris.reset_index(drop=True, inplace=True)

# BONUS: Tạo câu hỏi của riêng bạn và trả lời nó
# Câu hỏi: Giá trị trung bình của 'sepal_length' là bao nhiêu?
mean_sepal_length = iris['sepal_length'].mean()
print("Giá trị trung bình của 'sepal_length' là:", mean_sepal_length)

# Xuất kết quả để kiểm tra
print("Dataframe sau khi xử lý:\n", iris.head(), "\n")

#Wine
# Bước 1: Import các thư viện cần thiết
import pandas as pd
import numpy as np

# Bước 2: Import bộ dữ liệu từ địa chỉ
url = 'https://raw.githubusercontent.com/openai-code/datasets/main/wine.data'
wine = pd.read_csv(url, header=None)

# Bước 3: Gán nó vào biến có tên là wine
# (đã làm ở trên)

# Bước 4: Xóa cột thứ nhất, tư, bảy, chín, mười một, mười ba và mười bốn
wine.drop(columns=[0, 3, 6, 8, 10, 12, 13], inplace=True)

# Bước 5: Gán tên các cột như sau
wine.columns = ['alcohol', 'malic_acid', 'alcalinity_of_ash', 'magnesium', 'flavanoids', 'proanthocyanins', 'hue']

# Bước 6: Đặt giá trị của 3 hàng đầu tiên của cột alcohol thành NaN
wine.loc[0:2, 'alcohol'] = np.nan

# Bước 7: Đặt giá trị của các hàng 3 và 4 của cột magnesium thành NaN
wine.loc[3:4, 'magnesium'] = np.nan

# Bước 8: Điền giá trị NaN bằng số 10 trong cột alcohol và 100 trong cột magnesium
wine['alcohol'].fillna(10, inplace=True)
wine['magnesium'].fillna(100, inplace=True)

# Bước 9: Đếm số lượng giá trị bị thiếu
missing_values_count = wine.isnull().sum().sum()
print("Số lượng giá trị bị thiếu:", missing_values_count)

# Bước 10: Tạo một mảng gồm 10 số ngẫu nhiên từ 0 đến 10
random_indices = np.random.randint(0, len(wine), size=10)

# Bước 11: Sử dụng các số ngẫu nhiên bạn đã tạo làm chỉ mục và gán giá trị NaN cho mỗi ô
for i in random_indices:
    wine.iloc[i, np.random.randint(0, wine.shape[1])] = np.nan

# Bước 12: Có bao nhiêu giá trị bị thiếu?
missing_values_count_after_random = wine.isnull().sum().sum()
print("Số lượng giá trị bị thiếu sau khi gán ngẫu nhiên:", missing_values_count_after_random)

# Bước 13: Xóa các hàng chứa giá trị bị thiếu
wine.dropna(inplace=True)

# Bước 14: Chỉ in các giá trị không-null trong cột alcohol
print("Các giá trị không-null trong cột alcohol:\n", wine['alcohol'].dropna())

# Bước 15: Đặt lại chỉ mục để bắt đầu từ 0
wine.reset_index(drop=True, inplace=True)

# BONUS: Tạo câu hỏi của riêng bạn và trả lời nó
# Câu hỏi: Giá trị trung bình của 'flavanoids' là bao nhiêu sau khi xử lý?
mean_flavanoids = wine['flavanoids'].mean()
print("Giá trị trung bình của 'flavanoids' là:", mean_flavanoids)

# Xuất kết quả để kiểm tra
print("Dataframe sau khi xử lý:\n", wine.head(), "\n")
