import numpy as np

# Mảng 4x4
arr = np.arange(16).reshape(4, 4)
print("Mảng gốc:\n", arr)

print("1. Toàn bộ mảng:")
print(arr)

print("2. Hàng đầu tiên:")
print(arr[0])

print("3. Hàng thứ 2:")
print(arr[2])

print("4. Cột thứ 2:")
print(arr[:, 1])

print("5. Góc trên bên trái (2 hàng 2 cột):")
print(arr[:2, :2])

print("6. Góc trên bên phải (2 hàng, 2 cột cuối):")
print(arr[:2, 2:])

print("7. Đường chéo chính:")
print(arr[[0, 1, 2, 3], [0, 1, 2, 3]])

print("8. Đường chéo phụ:")
print(arr[[1, 2, 3], [3, 2, 1]])

print("9. Cột đầu và cuối:")
print(arr[:, [0, 3]])

print("10. Góc trên trái và góc dưới phải:")
print(arr[[1, 3], [0, 3]])

print("11. Hai cột đầu:")
print(arr[:, :2])

print("12. Ô vuông trung tâm 2x2:")
print(arr[1:3, 1:3])
