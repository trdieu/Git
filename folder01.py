#folder 01
import pandas as pd
import numpy as np

#ex2
# Bước 2: Nhập dữ liệu từ địa chỉ này
url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"
chipo = pd.read_csv(url, sep='\t')

# Bước 4: Xem 10 mục đầu tiên
print(chipo.head(10))

# Bước 5: Số lượng quan sát trong tập dữ liệu
# Giải pháp 1
num_observations = chipo.shape[0]
print(f"Số lượng quan sát: {num_observations}")

# Giải pháp 2
num_observations = len(chipo)
print(f"Số lượng quan sát: {num_observations}")

# Bước 6: Số lượng cột trong tập dữ liệu
num_columns = chipo.shape[1]
print(f"Số lượng cột: {num_columns}")

# Bước 7: In tên của tất cả các cột
print(chipo.columns)

# Bước 8: Chỉ số của tập dữ liệu
print(chipo.index)

# Bước 9: Món được đặt hàng nhiều nhất
most_ordered_item = chipo['item_name'].value_counts().idxmax()
print(f"Món được đặt hàng nhiều nhất: {most_ordered_item}")

# Bước 10: Số lượng món được đặt hàng nhiều nhất
most_ordered_item_count = chipo['item_name'].value_counts().max()
print(f"Số lượng món {most_ordered_item} đã được đặt: {most_ordered_item_count}")

# Bước 11: Món được đặt hàng nhiều nhất trong cột choice_description
most_ordered_choice = chipo['choice_description'].value_counts().idxmax()
print(f"Món được đặt hàng nhiều nhất trong cột choice_description: {most_ordered_choice}")

# Bước 12: Tổng số món đã được đặt
total_items_ordered = chipo['quantity'].sum()
print(f"Tổng số món đã được đặt: {total_items_ordered}")

# Bước 13: Chuyển giá món hàng sang kiểu float
# Bước 13.a: Kiểm tra kiểu của item_price
print(chipo['item_price'].dtype)

# Bước 13.b: Tạo hàm lambda và thay đổi kiểu của item_price
chipo['item_price'] = chipo['item_price'].apply(lambda x: float(x[1:]))

# Bước 13.c: Kiểm tra lại kiểu của item_price
print(chipo['item_price'].dtype)

# Bước 14: Doanh thu trong giai đoạn của tập dữ liệu
revenue = (chipo['quantity'] * chipo['item_price']).sum()
print(f"Doanh thu: {revenue}")

# Bước 15: Có bao nhiêu đơn hàng đã được thực hiện trong giai đoạn này
total_orders = chipo['order_id'].nunique()
print(f"Số lượng đơn hàng: {total_orders}")

# Bước 16: Doanh thu trung bình cho mỗi đơn hàng
# Giải pháp 1
average_revenue_per_order = revenue / total_orders
print(f"Doanh thu trung bình cho mỗi đơn hàng: {average_revenue_per_order}")

# Giải pháp 2
order_grouped = chipo.groupby('order_id').sum()
average_revenue_per_order = order_grouped['item_price'].mean()
print(f"Doanh thu trung bình cho mỗi đơn hàng: {average_revenue_per_order}")

# Bước 17: Có bao nhiêu món khác nhau đã được bán
different_items_sold = chipo['item_name'].nunique()
print(f"Số lượng món khác nhau đã được bán: {different_items_sold}")

#ex3
# Bước 2: Nhập dữ liệu từ địa chỉ này
url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user"
users = pd.read_csv(url, sep='|')

# Bước 3: Gán nó cho một biến gọi là users và sử dụng user_id làm chỉ số
users = users.set_index('user_id')

# Bước 4: Xem 25 mục đầu tiên
print(users.head(25))

# Bước 5: Xem 10 mục cuối cùng
print(users.tail(10))

# Bước 6: Số lượng quan sát trong tập dữ liệu
num_observations = users.shape[0]
print(f"Số lượng quan sát: {num_observations}")

# Bước 7: Số lượng cột trong tập dữ liệu
num_columns = users.shape[1]
print(f"Số lượng cột: {num_columns}")

# Bước 8: In tên của tất cả các cột
print(users.columns)

# Bước 9: Chỉ số của tập dữ liệu
print(users.index)

# Bước 10: Kiểu dữ liệu của mỗi cột
print(users.dtypes)

# Bước 11: Chỉ in cột occupation
print(users['occupation'])

# Bước 12: Có bao nhiêu nghề nghiệp khác nhau trong tập dữ liệu này
num_unique_occupations = users['occupation'].nunique()
print(f"Số lượng nghề nghiệp khác nhau: {num_unique_occupations}")

# Bước 13: Nghề nghiệp nào phổ biến nhất
most_frequent_occupation = users['occupation'].value_counts().idxmax()
print(f"Nghề nghiệp phổ biến nhất: {most_frequent_occupation}")

# Bước 14: Tóm tắt DataFrame
print(users.describe())

# Bước 15: Tóm tắt tất cả các cột
print(users.describe(include='all'))

# Bước 16: Chỉ tóm tắt cột occupation
print(users['occupation'].describe())

# Bước 17: Tuổi trung bình của người dùng
mean_age = users['age'].mean()
print(f"Tuổi trung bình của người dùng: {mean_age}")

# Bước 18: Tuổi nào có tần suất xuất hiện ít nhất
least_occurrence_age = users['age'].value_counts().idxmin()
print(f"Tuổi có tần suất xuất hiện ít nhất: {least_occurrence_age}")

#ex1
import pandas as pd

# Đường dẫn đến tệp tsv đã giải nén
file_path = "test.tsv"
food = pd.read_csv(file_path, sep='\t')

# Bước 4: Xem 5 mục đầu tiên
print(food.head(5))

# Bước 5: Số lượng quan sát trong tập dữ liệu
num_observations = food.shape[0]
print(f"Số lượng quan sát: {num_observations}")

# Bước 6: Số lượng cột trong tập dữ liệu
num_columns = food.shape[1]
print(f"Số lượng cột: {num_columns}")

# Bước 7: In tên của tất cả các cột
print(food.columns)

# Bước 8: Tên của cột thứ 105
column_105_name = food.columns[104]
print(f"Tên của cột thứ 105: {column_105_name}")

# Bước 9: Kiểu dữ liệu của các quan sát trong cột thứ 105
column_105_dtype = food.dtypes[104]
print(f"Kiểu dữ liệu của cột thứ 105: {column_105_dtype}")

# Bước 10: Chỉ số của tập dữ liệu
print(food.index)

# Bước 11: Tên sản phẩm của quan sát thứ 19
product_name_19th = food.iloc[18]['product_name']
print(f"Tên sản phẩm của quan sát thứ 19: {product_name_19th}")

