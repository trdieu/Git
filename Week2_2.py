# bai 1
def average(a, b, c, d, e):
    tong = a + b + c + d + e
    tb = tong/5
    return tb

a = int(input("nhap so a = "))
b = int(input("nhap so b = "))
c = int(input("nhap so c = "))
d = int(input("nhap so d = "))
e = int(input("nhap so e = "))

print("Trung binh cong cua ham la: ", average(a, b, c, d, e))

#bai 2
def area(a, b, c):
    p = (a + b + c) / 2
    dt = (p*(p-a)*(p-b)*(p-c))**0.5
    return dt

a = int(input("nhap do dai canh thu nhat: "))
b = int(input("nhap do dai canh thu hai: "))
c = int(input("nhap do dai canh thu ba: "))

print("Dien tich tam giac la: ", area(a, b, c))

#bai 3
def area2(x1, y1, x2, y2, x3, y3):
    return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

def main():
    # Lấy tọa độ từ người dùng
    x1, y1 = map(int, input("Nhập tọa độ đỉnh thứ nhất (x1, y1): ").split())
    x2, y2 = map(int, input("Nhập tọa độ đỉnh thứ hai (x2, y2): ").split())
    x3, y3 = map(int, input("Nhập tọa độ đỉnh thứ ba (x3, y3): ").split())

    # Tính diện tích
    area = area2(x1, y1, x2, y2, x3, y3)
    print(f"Diện tích tam giác là: {area:.2f}")

if __name__ == "__main__":
    main()

#bai 4
def total(N):
    tong_so = 0
    while N != 0:
        tong_so += N % 10
        N //= 10
    return tong_so


if __name__ == "__main__":
    N = int(input("Nhập số nguyên N: "))
    result = total(N)
    print(f"Tổng các chữ số của {N} là: {result}")

#bai 5
import math

def is_perfect_square(x):
    s = int(math.sqrt(x))
    return s * s == x

def isFibo(N):
    # Kiểm tra tính chính phương của 5N^2 + 4 hoặc 5N^2 - 4
    return is_perfect_square(5 * N * N + 4) or is_perfect_square(5 * N * N - 4)

    # Chương trình chính để kiểm tra hàm isFibo
if __name__ == "__main__":
    N = int(input("Nhập số nguyên N: "))
    if isFibo(N):
        print(f"{N} là số Fibonacci")
    else:
        print(f"{N} không phải là số Fibonacci")

#bai 6
import math

def tinh_gia_tri_F(N):
    tong = 0
    for i in range(1, N + 1):
        tong += math.factorial(i)
    return tong

if __name__ == "__main__":
    N = int(input("Nhập số nguyên dương N: "))
    if N > 0:
        ket_qua = tinh_gia_tri_F(N)
        print(f"Giá trị của F({N}) là: {ket_qua}")
    else:
        print("N phải là số nguyên dương lớn hơn 0.")

#bai 7
def danh_gia_ket_qua_hoc_tap(diem_tb):
    if diem_tb < 3.5:
        return "xếp loại yếu"
    elif diem_tb < 5:
        return "xếp loại kém"
    elif diem_tb < 6.5:
        return "xếp loại trung bình"
    elif diem_tb < 8:
        return "xếp loại khá"
    elif diem_tb < 9:
        return "xếp loại giỏi"
    else:
        return "xếp loại xuất sắc"

if __name__ == "__main__":
    diem_tb = float(input("Nhập điểm trung bình học tập của sinh viên: "))
    ket_qua = danh_gia_ket_qua_hoc_tap(diem_tb)
    print(f"Đánh giá kết quả học tập của sinh viên: {ket_qua}")

#bai 8
def tim_gia_tri_lon_nhat(a, b, c):
    if a >= b and a >= c:
        lon_nhat = a
    elif b >= a and b >= c:
        lon_nhat = b
    else:
        lon_nhat = c
    return lon_nhat

def tim_gia_tri_thu_ba(a, b, c, lon_nhat):
    if (a == b and a == lon_nhat) or (a == c and a == lon_nhat) or (b == c and b == lon_nhat):
        if a == lon_nhat:
            gia_tri_con_lai = b if b != lon_nhat else c
        elif b == lon_nhat:
            gia_tri_con_lai = a if a != lon_nhat else c
        else:
            gia_tri_con_lai = a if a != lon_nhat else b
        return gia_tri_con_lai
    return None

if __name__ == "__main__":
    a = int(input("Nhập số thứ nhất a: "))
    b = int(input("Nhập số thứ hai b: "))
    c = int(input("Nhập số thứ ba c: "))

    lon_nhat = tim_gia_tri_lon_nhat(a, b, c)
    print(f"Giá trị lớn nhất trong 3 số là: {lon_nhat}")

    gia_tri_thu_ba = tim_gia_tri_thu_ba(a, b, c, lon_nhat)
    if gia_tri_thu_ba is not None:
        print(f"Giá trị thứ 3 còn lại là: {gia_tri_thu_ba}")
    else:
        print("Không có ít nhất hai số cùng nhận giá trị lớn nhất.")

#bai 9
def la_nam_nhuan(nam):
    # Kiểm tra năm nhuận
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        return True
    else:
        return False

def ngay_trong_thang(thang, nam):
    # Số ngày trong mỗi tháng
    if thang == 2:
        if la_nam_nhuan(nam):
            return 29
        else:
            return 28
    elif thang in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def ngay_tiep_theo(d, m, y):
    # Tính ngày tiếp theo
    ngay_trong_t = ngay_trong_thang(m, y)
    
    if d < ngay_trong_t:
        d += 1
    else:
        d = 1
        if m < 12:
            m += 1
        else:
            m = 1
            y += 1
            
    return d, m, y

if __name__ == "__main__":
    d = int(input("Nhập ngày: "))
    m = int(input("Nhập tháng: "))
    y = int(input("Nhập năm: "))

    ngay_tiep, thang_tiep, nam_tiep = ngay_tiep_theo(d, m, y)
    print(f"Ngày tiếp theo của {d}/{m}/{y} là: {ngay_tiep}/{thang_tiep}/{nam_tiep}")
