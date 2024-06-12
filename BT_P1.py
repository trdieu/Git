#bai 2
P = 10000000
r = 0.05
n = 1
t = 10

# Tính số tiền sau 10 năm
A = P * (1 + r / n) ** (n * t)
print(f"Số tiền sau 10 năm: {A:.2f} đồng")

# Tính số năm cần thiết để có ít nhất 50 triệu đồng
so_tien_mt = 50000000
nam = 0
so_tien_ht = P

while so_tien_ht < so_tien_mt:
    nam += 1
    so_tien_ht = P * (1 + r / n) ** (n * nam)

print(f"Số năm cần thiết để có ít nhất 50 triệu đồng: {nam} năm")


#bai 3
n = int(input("nhap so nguyen n = "))
print("n o dang nhi phan la: ", bin(n))
print("n o dang bat phan la: ", oct(n))
print("n o dang thap luc phan la: ", hex(n))

#bai 4
a = int(input("nhap so nguyen a = "))
b = int(input("nhap so nguyen b = "))

x = a**(1/b)
print("x = ", x)

#bai 5
X = int(input("nhap so nguyen X = "))

def chuyen_sang_chuoi(X):
    X_str = str(abs(X))
    so = len(X_str)
    dau_tien = X_str[0]

    return so, dau_tien

so, dau_tien = chuyen_sang_chuoi(X)

print("so X co", so, "chu so")
print("chu so dau tien cua X la: ", dau_tien)

