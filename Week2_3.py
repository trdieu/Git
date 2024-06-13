#bai 1
chuoi = input("Nhập chuỗi các từ tiếng Anh: ")
cac_tu = chuoi.split()

cac_tu.sort()

print("Các từ theo thứ tự từ điển:")
for tu in cac_tu:
    print(tu)

#bai 2
def la_so_nhi_phan(so):
    return all(ky_tu in '01' for ky_tu in so)

chuoi = input("Nhập chuỗi các số nhị phân, cách nhau bởi dấu phẩy: ")
cac_so_nhi_phan = chuoi.split(',')

print("Các giá trị số nhị phân hợp lệ được nhập:")
for so in cac_so_nhi_phan:
    so = so.strip()
    if la_so_nhi_phan(so):
        print(so)

#bai 3
def tong_uoc_so(x):
    return sum(i for i in range(1, x) if x % i == 0)

n = int(input("Nhập số n: "))

print("Các số nguyên dương nhỏ hơn", n, "có tổng các ước số lớn hơn chính nó:")
for i in range(1, n):
    if tong_uoc_so(i) > i:
        print(i)

#bai 4
import re

email = input("Nhập địa chỉ email: ")

mau_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

if re.match(mau_email, email):
    print("Địa chỉ email hợp lệ.")
else:
    print("Địa chỉ email không hợp lệ.")

#bai 5
def tam_giac_pascal(n):
    tam_giac = [[1]]
    for i in range(1, n):
        hang_moi = [1]
        hang_truoc = tam_giac[-1]
        for j in range(1, i):
            hang_moi.append(hang_truoc[j-1] + hang_truoc[j])
        hang_moi.append(1)
        tam_giac.append(hang_moi)
    return tam_giac

n = int(input("Nhập số dòng n: "))
tam_giac = tam_giac_pascal(n)

for hang in tam_giac:
    print(hang)

#bai 6
def fibonacci_duoi_n(n):
    fibonacci = [0, 1]
    while True:
        so_tiep_theo = fibonacci[-1] + fibonacci[-2]
        if so_tiep_theo >= n:
            break
        fibonacci.append(so_tiep_theo)
    return fibonacci

n = int(input("Nhập số nguyên n: "))
day_fibonacci = fibonacci_duoi_n(n)

print("Dãy Fibonacci nhỏ hơn", n, "là:", day_fibonacci)

#bai 7
def so_nguyen_to(n):
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n, i):
                is_prime[j] = False
    return [i for i in range(n) if is_prime[i]]

P = tuple(so_nguyen_to(1000000))

print("Tuple P chứa các số nguyên tố nhỏ hơn 1 triệu là:", P)
