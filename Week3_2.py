#bai 1
# Định nghĩa từ điển D
D = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}

# In ra các value của D theo thứ tự tăng dần của key
for key in sorted(D.keys()):
    print(D[key])

#bai 2
# Nhập từ điển D (ví dụ)
D = {
    'a': 'apple',
    'b': 'banana',
    'c': 'apple',
    'd': 'date',
    'e': 'banana'
}

# In ra các value khác nhau trong từ điển
unique_values = set(D.values())
for value in unique_values:
    print(value)

#bai 3
# Nhập từ điển D (ví dụ)
D = {
    'a': 10,
    'b': 30,
    'c': 20,
    'd': 50,
    'e': 40
}

# Lấy ra 3 giá trị lớn nhất
top_3_values = sorted(D.values(), reverse=True)[:3]

# In ra 3 giá trị lớn nhất
for value in top_3_values:
    print(value)

#bai 4
# Nhập chuỗi S từ bàn phím
S = input("Nhập chuỗi S: ")

# Tạo từ điển D
D = {}
for char in S:
    if char in D:
        D[char] += 1
    else:
        D[char] = 1

# In ra từ điển D
print(D)

#bai 5
# Nhập từ điển prices và stock
prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
stock = {"banana": 6, "orange": 32, "pear": 15}

# Tạo từ điển lưu trữ tổng giá trị của từng loại trái cây
total_value = {fruit: prices.get(fruit, 0) * stock.get(fruit, 0) for fruit in prices}

# Sắp xếp và in ra kết quả
sorted_fruits = sorted(total_value.items(), key=lambda item: item[1], reverse=True)

for fruit, value in sorted_fruits:
    print(f"{fruit} {value}")

#bai 6
import random

# Tạo từ điển lưu lượng mưa trung bình
rainfall_data = {month: [random.uniform(100, 4000) for _ in range(20)] for month in range(1, 13)}

# In ra từ điển
for month, rainfall in rainfall_data.items():
    print(f"Tháng {month}: {rainfall} \n")

#bai 7
# Nhập từ điển A và B (ví dụ)
A = {'a': 1, 'b': 2, 'c': 3}
B = {'b': 4, 'c': 2, 'd': 5}

# Tạo từ điển C
C = {}

# Thêm các cặp (key, value) từ A vào C
for key, value in A.items():
    C[key] = value

# Thêm hoặc cập nhật các cặp (key, value) từ B vào C
for key, value in B.items():
    if key in C:
        C[key] = max(C[key], value)
    else:
        C[key] = value

# In ra từ điển C
print(C)