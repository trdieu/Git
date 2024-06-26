import numpy as np

#bai 1
array_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
array_2x3 = np.array([[1, 2, 5],
                      [7, 10, 7]])
MT_3x3 = np.array([[1., 0., 0.],
                                [0., 1., 0.],
                                [0., 0., 1.]])
array_4d = np.random.uniform(-1, 2, size=(3, 2, 5, 4))

print(array_1d, "\n")
print(array_2x3, "\n")
print(MT_3x3, "\n")
print(array_4d, "\n")

#bai 2
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
element_2nd_row_3rd_col = arr[1, 2]
first_two_rows = arr[:2, :]
last_column = arr[:, -1]
square_matrix = arr[[0, 2], :][:, [0, 2]]

print(element_2nd_row_3rd_col, "\n")
print(first_two_rows, "\n")
print(last_column, "\n")
print(square_matrix, "\n")

#bai 3
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
sum_ab = a + b
c = a ** 2
tich_vo_huong = np.dot(a, b)
print(sum_ab, "\n")
print(c, "\n")
print(tich_vo_huong, "\n")

#bai 4
x = np.array([[1, 2], [3, 4]])
x = np.array([[1, 2], [3, 4]])
x_reshaped = x.reshape((4, 1))
y_horizontal = np.array([[5, 6]])
x_horizontal_concat = np.hstack((x, y_horizontal.T))
y_vertical = np.array([[5, 6]])
x_vertical_concat = np.vstack((x, y_vertical))

print(x_reshaped, "\n")
print(x_horizontal_concat, "\n")
print(x_vertical_concat, "\n")

#bai 5
import numpy as np

A = np.random.randint(-5, 11, size=(5, 7))

sum_A = np.sum(A)

min_in_columns = np.min(A, axis=0)
max_in_columns = np.max(A, axis=0)

std_in_rows = np.std(A, axis=1)

var_in_columns = np.var(A, axis=0)

import numpy as np

A = np.random.randint(-5, 11, size=(5, 7))

sum_A = np.sum(A)

min_in_columns = np.min(A, axis=0)
max_in_columns = np.max(A, axis=0)

std_in_rows = np.std(A, axis=1)

var_in_columns = np.var(A, axis=0)

range_in_columns = max_in_columns - min_in_columns

print(sum_A, "\n")
print("min: ", min_in_columns, "\n" "max: ", max_in_columns, "\n")
print(std_in_rows, "\n")
print(var_in_columns, "\n")
print(range_in_columns, "\n")

#bai 6
x = np.array([1, 2, 3])

x_plus_5 = x + 5
print("x + 5 =", x_plus_5, "\n")
Y = np.random.rand(3, 3)
Y_times_2 = Y * 2
print("Y =", Y, "\n")
print("Y * 2 =", Y_times_2, "\n")
Z = np.random.rand(3, 5)
result = np.dot(Y, Z)
print("Z =", Z, "\n")
print("Y x Z =", result, "\n")

#bai 7
# Tạo mảng arr từ 1 đến 100
arr = np.arange(1, 101)

# 1) Lớn hơn giá trị trung bình của mảng
mean_value = np.mean(arr)
greater_than_mean = arr[arr > mean_value]
print("Lớn hơn giá trị trung bình của mảng:", greater_than_mean, "\n")

# 2) Bé hơn giá trị Q1 (Tứ phân vị thứ 1)
q1_value = np.percentile(arr, 25)
less_than_q1 = arr[arr < q1_value]
print("Bé hơn giá trị Q1:", less_than_q1, "\n")

# 3) Lớn hơn giá trị Q3 (Tứ phân vị thứ 3)
q3_value = np.percentile(arr, 75)
greater_than_q3 = arr[arr > q3_value]
print("Lớn hơn giá trị Q3:", greater_than_q3, "\n")

# 4) Chia hết cho 2 nhưng không chia hết cho 3
divisible_by_2_not_3 = arr[(arr % 2 == 0) & (arr % 3 != 0)]
print("Chia hết cho 2 nhưng không chia hết cho 3:", divisible_by_2_not_3, "\n")

# 5) Chia hết cho 5 nhưng không chia hết cho 2
divisible_by_5_not_2 = arr[(arr % 5 == 0) & (arr % 2 != 0)]
print("Chia hết cho 5 nhưng không chia hết cho 2:", divisible_by_5_not_2, "\n")

# 6) Các số lẻ nhưng không chia hết cho 3
odd_not_3 = arr[(arr % 2 != 0) & (arr % 3 != 0)]
print("Các số lẻ nhưng không chia hết cho 3:", odd_not_3, "\n")

# 7) Các số chẵn nhưng không chia hết cho 5
even_not_5 = arr[(arr % 2 == 0) & (arr % 5 != 0)]
print("Các số chẵn nhưng không chia hết cho 5:", even_not_5, "\n")

#bai 8
# Tạo mảng với 50 giá trị nằm trong khoảng từ 0 đến 10
linspace_array = np.linspace(0, 10, 50)
print("Mảng linspace:", linspace_array, "\n")
# Tạo một mảng ngẫu nhiên
arr = np.random.randint(0, 10, size=10)
print("Mảng ban đầu:", arr, "\n")

# Sử dụng np.where để thay thế các giá trị
modified_arr = np.where(arr < 5, 0, 1)
print("Mảng sau khi thay thế:", modified_arr, "\n")
# Tạo một mảng ngẫu nhiên
arr = np.random.randint(0, 10, size=10)
print("Mảng ban đầu:", arr, "\n")

# Sử dụng np.where để thay thế các giá trị
modified_arr = np.where(arr < 5, 0, 1)
print("Mảng sau khi thay thế:", modified_arr, "\n")
# Tạo một mảng
arr = np.array([10, 20, 30, 40, 50])

# Lấy ngẫu nhiên một phần tử từ mảng
random_choice = np.random.choice(arr)
print("Phần tử ngẫu nhiên được chọn:", random_choice, "\n")
# Hệ phương trình tuyến tính Ax = b
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])

# Giải hệ phương trình
x = np.linalg.solve(A, b)
print("Nghiệm của hệ phương trình:", x, "\n")
# Tạo hai mảng
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Sử dụng np.concatenate
concat_result = np.concatenate((a, b))
print("Kết quả của np.concatenate:", concat_result, "\n")

# Sử dụng np.vstack (xếp chồng theo chiều dọc)
vstack_result = np.vstack((a, b))
print("Kết quả của np.vstack:", vstack_result, "\n")

# Sử dụng np.hstack (xếp chồng theo chiều ngang)
hstack_result = np.hstack((a, b))
print("Kết quả của np.hstack:", hstack_result, "\n")
# np.linspace tạo ra các giá trị trong khoảng đều nhau
linspace_example = np.linspace(1, 10, 10)
print("np.linspace:", linspace_example, "\n")

# np.logspace tạo ra các giá trị theo lũy thừa cơ số 10
logspace_example = np.logspace(1, 3, 10)
print("np.logspace:", logspace_example, "\n")
# Tạo một mảng với các giá trị lặp lại
arr = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])

# Lọc các giá trị duy nhất
unique_values, counts = np.unique(arr, return_counts=True)
print("Giá trị duy nhất:", unique_values, "\n")
print("Số lần xuất hiện:", counts, "\n")

#bai 9
# Định nghĩa ma trận A và B
A = np.array([[10, 1, 2],
              [9, 7, 4],
              [0, 2, 1]])

B = np.array([[2, 3, 4],
              [0, 4, 2],
              [3, 2, 1]])

# 1. Tính tích AB
AB = np.dot(A, B)
print("AB =", AB)

# 2. Tính tích B(A^T)AB
AT = np.transpose(A)
B_AT_AB = np.dot(B, np.dot(AT, AB))
print("B(A^T)AB =", B_AT_AB)

# 3. Tính tích (AB^T)B(AT)
BT = np.transpose(B)
ABT_B_AT = np.dot(np.dot(A, BT), AT)
print("AB^TB(AT) =", ABT_B_AT)

# Nhận xét về kết quả biểu thức 3 và 2
# Biểu thức 3 khác biệt so với biểu thức 2 về kích thước và giá trị do thứ tự nhân ma trận khác nhau

# Tính các phép toán ma trận
rank_A = np.linalg.matrix_rank(A)
det_A = np.linalg.det(A)
A_inv = np.linalg.inv(A)
trace_A = np.trace(A)

print("Rank của A =", rank_A, "\n")
print("Định thức của A =", det_A, "\n")
print("Nghịch đảo của A =", A_inv, "\n")
print("Trace của A =", trace_A, "\n")

# Biến đổi shape ma trận
# Concatenate ma trận A và ma trận B theo dòng
concatenated_matrix = np.concatenate((A, B), axis=0)
print("Ma trận sau khi concatenate theo dòng:", concatenated_matrix, "\n")

# Reshape ma trận A thành vector
reshaped_A = A.reshape(-1)
print("Ma trận A sau khi reshape thành vector:", reshaped_A, "\n")

# Phân phối xác suất sau khi đi qua hàm softmax các dòng của A
def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=1, keepdims=True)

softmax_A = softmax(A)
print("Softmax của A:", softmax_A, "\n")

# Tìm ra nhãn dự báo cho mỗi dòng (giá trị lớn nhất trên mỗi dòng của softmax_A)
predicted_labels = np.argmax(softmax_A, axis=1)
print("Nhãn dự báo cho mỗi dòng của A:", predicted_labels, "\n")

# Tính tổng, trung bình, min, max của mỗi dòng
sum_rows = np.sum(A, axis=1)
mean_rows = np.mean(A, axis=1)
min_rows = np.min(A, axis=1)
max_rows = np.max(A, axis=1)

print("Tổng của mỗi dòng:", sum_rows, "\n")
print("Trung bình của mỗi dòng:", mean_rows, "\n")
print("Min của mỗi dòng:", min_rows, "\n")
print("Max của mỗi dòng:", max_rows, "\n")
