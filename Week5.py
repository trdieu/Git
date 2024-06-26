import numpy as np

#bai 2
# Định nghĩa hai mảng a và b
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
b = np.array([4, 5, 6, 10, 11])

# Tìm các phần tử nằm trong a mà không nằm trong b
difference = np.setdiff1d(a, b)

# Sắp xếp các phần tử theo thứ tự từ bé đến lớn
sorted_difference = np.sort(difference)

# In kết quả
print("Các phần tử nằm trong a mà không nằm trong b, sắp xếp theo thứ tự từ bé đến lớn:")
print(sorted_difference)

#bai 2
# Tạo một mảng đa chiều ngẫu nhiên để minh họa
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Tìm chỉ số của giá trị lớn nhất và nhỏ nhất trên trục 0 (theo các hàng)
max_indices_axis0 = np.argmax(arr, axis=0)
min_indices_axis0 = np.argmin(arr, axis=0)

# Tìm chỉ số của giá trị lớn nhất và nhỏ nhất trên trục 1 (theo các cột)
max_indices_axis1 = np.argmax(arr, axis=1)
min_indices_axis1 = np.argmin(arr, axis=1)

print("Chỉ số của giá trị lớn nhất trên trục 0:", max_indices_axis0)
print("Chỉ số của giá trị nhỏ nhất trên trục 0:", min_indices_axis0)
print("Chỉ số của giá trị lớn nhất trên trục 1:", max_indices_axis1)
print("Chỉ số của giá trị nhỏ nhất trên trục 1:", min_indices_axis1)
