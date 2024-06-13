#bai 1
chuoi = input("Nhập chuỗi: ")
if not chuoi.endswith("!!!"):
    chuoi += "!!!"
print(chuoi)

#bai 2
day_so = input("Nhập dãy số: ")
print("Dãy số vừa nhập:", day_so)

#bai 3
ten_day_du = input("Nhập tên người: ")
ho, ten = ten_day_du.split()
print("Họ:", ho)
print("Tên riêng:", ten)

#bai 4
chuoi = input("Nhập chuỗi: ")
chuoi_khong_so = ''.join([ky_tu for ky_tu in chuoi if not ky_tu.isdigit()])
print("Chuỗi sau khi loại bỏ các chữ số:", chuoi_khong_so)

#bai 5
day_tu = input("Nhập dãy các từ: ").split()
do_dai_max = max(len(tu) for tu in day_tu)
tu_dai_nhat = [tu for tu in day_tu if len(tu) == do_dai_max]
print("Từ dài nhất:", ', '.join(tu_dai_nhat))

#bai 6
day_tu = input("Nhập dãy các từ: ")
tan_suat = {}
for ky_tu in day_tu:
    if ky_tu.isalpha():
        tan_suat[ky_tu] = tan_suat.get(ky_tu, 0) + 1

for ky_tu, so_lan in tan_suat.items():
    print(f"Chữ '{ky_tu}' xuất hiện {so_lan} lần")

#bai 7
def xoa_ky_tu_de_lam_lon_nhat(S, N):
    stack = []
    so_luong_da_xoa = 0

    for ky_tu in S:
        while stack and so_luong_da_xoa < N and stack[-1] < ky_tu:
            stack.pop()
            so_luong_da_xoa += 1
        stack.append(ky_tu)

    while so_luong_da_xoa < N:
        stack.pop()
        so_luong_da_xoa += 1

    ket_qua = ''.join(stack)
    return ket_qua

S = input("Nhập chuỗi S (chỉ gồm chữ số): ")
N = int(input("Nhập số nguyên N: "))

ket_qua = xoa_ky_tu_de_lam_lon_nhat(S, N)
print("Chuỗi sau khi xóa", N, "ký tự để được số lớn nhất là:", ket_qua)

#bai 8
chuoi_S = input("Nhập chuỗi S: ")

bang_chuyen_doi = str.maketrans('0123456789', '?'*10)

chuoi_S_moi = chuoi_S.translate(bang_chuyen_doi)

print("Chuỗi sau khi thay thế các chữ số:", chuoi_S_moi)

#bai 9
chuoi_S = input("Nhập chuỗi S: ")

if chuoi_S == chuoi_S[::-1]:
    print("Chuỗi", chuoi_S, "là chuỗi đối xứng.")
else:
    print("Chuỗi", chuoi_S, "không phải là chuỗi đối xứng.")