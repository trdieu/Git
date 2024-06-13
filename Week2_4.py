#bai 1
tap_hop = set(range(100))
print("Tập hợp các phần tử từ 0 đến 99 là:", tap_hop)

#bai 2
tap_hop_le = set(range(1, 200, 2))
print("Tập hợp các số nguyên lẻ từ 1 đến 199 là:", tap_hop_le)

#bai 3
chuoi_so = input("Nhập các số, cách nhau bởi dấu cách: ")
tap_hop = set(map(int, chuoi_so.split()))

print("Các phần tử của tập hợp là:", tap_hop)

max_value = max(tap_hop)
min_value = min(tap_hop)
print("Giá trị lớn nhất trong tập hợp là:", max_value)
print("Giá trị nhỏ nhất trong tập hợp là:", min_value)

#bai 4
ho_ten_sinh_vien = set()

print("Nhập họ và tên đầy đủ của các sinh viên (mỗi người trên một dòng, kết thúc bằng dòng trống):")
while True:
    ho_ten = input().strip()
    if ho_ten == "":
        break
    ho_ten_sinh_vien.add(ho_ten)

print("\nDanh sách họ và tên của sinh viên trong lớp:")
for ho_ten in ho_ten_sinh_vien:
    print(ho_ten)

#bai 5
def uoc_so(N):
    if N <= 0:
        return "N phải là số nguyên dương"
    uoc = set()
    for i in range(1, N+1):
        if N % i == 0:
            uoc.add(i)
    return uoc

N = int(input("Nhập số nguyên N (> 0): "))

tap_hop_uoc = uoc_so(N)

print(f"Các ước số dương của {N} là:", tap_hop_uoc)

#bai 6
def uoc_so_chung(a, b):
    if a <= 0 or b <= 0:
        return "Cả hai số a và b phải là số nguyên dương"
    
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    
    ucln = gcd(a, b)
    uoc_chung = set()
    
    for i in range(1, ucln + 1):
        if ucln % i == 0:
            uoc_chung.add(i)
    
    return uoc_chung

a = int(input("Nhập số nguyên a (> 0): "))
b = int(input("Nhập số nguyên b (> 0): "))

tap_hop_uoc_chung = uoc_so_chung(a, b)

print(f"Các ước số chung của {a} và {b} là:", tap_hop_uoc_chung)

#bai 7
day_so = input("Nhập dãy số nguyên, cách nhau bởi dấu chấm phẩy (;): ")

cac_so = day_so.split(';')

cac_so = [so.strip() for so in cac_so if so.strip()]

so_khac_nhau = set(cac_so)

so_luong_so_khac_nhau = len(so_khac_nhau)

print(f"Số lượng số khác nhau trong dãy là: {so_luong_so_khac_nhau}")

#bai 8
def la_ve_thang(bo_so_nguoi_choi, bo_so_giai_dac_biet):
    tap_hop_nguoi_choi = set(bo_so_nguoi_choi)
    tap_hop_giai_dac_biet = set(bo_so_giai_dac_biet)

    so_luong_trung = len(tap_hop_nguoi_choi.intersection(tap_hop_giai_dac_biet))

    return so_luong_trung >= 5

N = int(input("Nhập số lượng bộ số người chơi: "))

bo_so_nguoi_choi_list = []
for i in range(N):
    bo_so_nguoi_choi = input(f"Nhập bộ số thứ {i + 1} (6 số, cách nhau bởi dấu cách): ").strip().split()
    bo_so_nguoi_choi_list.append(set(map(int, bo_so_nguoi_choi)))

bo_so_giai_dac_biet = input("Nhập bộ số giải đặc biệt (6 số, cách nhau bởi dấu cách): ").strip().split()
bo_so_giai_dac_biet = set(map(int, bo_so_giai_dac_biet))

nguoi_thang_cuoc = None
for i, bo_so_nguoi_choi in enumerate(bo_so_nguoi_choi_list, 1):
    if la_ve_thang(bo_so_nguoi_choi, bo_so_giai_dac_biet):
        nguoi_thang_cuoc = i
        print(f"Người chơi thứ {nguoi_thang_cuoc} thắng cuộc với bộ số: {' '.join(map(str, sorted(bo_so_nguoi_choi)))}")

if nguoi_thang_cuoc is None:
    print("Không có người chơi nào thắng cuộc.")

#bai 9
# a. Nhập danh sách mã nhân viên của cả 3 phòng
input_str = input("Nhập danh sách mã nhân viên của cả 3 phòng (cách nhau bởi dấu phẩy): ")
phong_nhan_su, phong_hanh_chinh, phong_truyen_thong = map(set, input_str.split(','))

# b. Số lượng nhân viên mỗi phòng
so_luong_nhan_vien_phong_nhan_su = len(phong_nhan_su)
so_luong_nhan_vien_phong_hanh_chinh = len(phong_hanh_chinh)
so_luong_nhan_vien_phong_truyen_thong = len(phong_truyen_thong)

# c. In ra số lượng nhân viên của mỗi phòng
print(f"a. Ba phòng ban này sử dụng tổng cộng {so_luong_nhan_vien_phong_nhan_su + so_luong_nhan_vien_phong_hanh_chinh + so_luong_nhan_vien_phong_truyen_thong} nhân viên.")
print(f"   - Phòng Nhân sự: {so_luong_nhan_vien_phong_nhan_su} nhân viên")
print(f"   - Phòng Hành chính: {so_luong_nhan_vien_phong_hanh_chinh} nhân viên")
print(f"   - Phòng Truyền thống: {so_luong_nhan_vien_phong_truyen_thong} nhân viên")

# d. In ra danh sách các mã nhân viên chỉ thuộc 1 phòng
nhan_vien_mot_phong = phong_nhan_su.symmetric_difference(phong_hanh_chinh).symmetric_difference(phong_truyen_thong)
print(f"d. Danh sách các mã nhân viên chỉ thuộc 1 phòng: {sorted(nhan_vien_mot_phong)}")

# e. Tìm và in ra các cặp phòng dùng chung nhiều nhân viên nhất
phong_cung_dung_nhieu_nhan_vien_nhat = []
max_so_luong_nhan_vien_chung = 0

# Tìm cặp phòng dùng chung nhiều nhân viên nhất
for pair in [('Nhân sự', 'Hành chính'), ('Nhân sự', 'Truyền thống'), ('Hành chính', 'Truyền thống')]:
    so_luong_nhan_vien_chung = len(phong_nhan_su.intersection(phong_hanh_chinh).intersection(phong_truyen_thong))
    
    if so_luong_nhan_vien_chung > max_so_luong_nhan_vien_chung:
        max_so_luong_nhan_vien_chung = so_luong_nhan_vien_chung
        phong_cung_dung_nhieu_nhan_vien_nhat = [pair]
    elif so_luong_nhan_vien_chung == max_so_luong_nhan_vien_chung:
        phong_cung_dung_nhieu_nhan_vien_nhat.append(pair)

print("e. Các cặp phòng dùng chung nhiều nhân viên nhất là:")
for pair in phong_cung_dung_nhieu_nhan_vien_nhat:
    print(f"   - {pair[0]} và {pair[1]}")

# f. In ra mã nhân viên đầu tiên của từng phòng (mã nhỏ nhất)
print(f"f. Mã nhân viên đầu tiên của từng phòng:")
print(f"   - Phòng Nhân sự: {min(phong_nhan_su)}")
print(f"   - Phòng Hành chính: {min(phong_hanh_chinh)}")
print(f"   - Phòng Truyền thống: {min(phong_truyen_thong)}")