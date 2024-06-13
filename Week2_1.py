#bai 1
def is_prime(N):
    if N <= 1:
        return False
    if N <= 3:
        return True
    if N % 2 == 0 or N % 3 == 0:
        return False
    
    i = 5
    while i * i <= N:
        if N % i == 0 or N % (i + 2) == 0:
            return False
        i += 6
    
    return True

try:
    N = int(input("Nhập một số nguyên: "))
    if is_prime(N):
        print(f"{N} là số nguyên tố.")
    else:
        print(f"{N} không phải là số nguyên tố.")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")

#bai 2
def is_prime(N):
    if N <= 1:
        return False
    if N <= 3:
        return True
    if N % 2 == 0 or N % 3 == 0:
        return False
    i = 5
    while i * i <= N:
        if N % i == 0 or N % (i + 2) == 0:
            return False
        i += 6
    return True

A = int(input("Nhập số nguyên A: "))
B = int(input("Nhập số nguyên B: "))

if A > B:
    print("A phải nhỏ hơn hoặc bằng B")
else:
    primes = [x for x in range(A, B + 1) if is_prime(x)]
    print(f"Các số nguyên tố trong khoảng [{A}, {B}]: {primes}")

#bai 3
import math

A = int(input("Nhập số nguyên dương A: "))
B = int(input("Nhập số nguyên dương B: "))

uscln = math.gcd(A, B)
bscnn = A * B // uscln

print(f"Ước số chung lớn nhất của {A} và {B} là: {uscln}")
print(f"Bội số chung nhỏ nhất của {A} và {B} là: {bscnn}")

#bai 4
import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

numbers = []
while True:
    n = int(input("Nhập số tự nhiên (kết thúc khi nhập số âm hoặc 0): "))
    if n <= 0:
        break
    numbers.append(n)

if numbers:
    uscln = numbers[0]
    bscnn = numbers[0]
    for num in numbers[1:]:
        uscln = gcd(uscln, num)
        bscnn = lcm(bscnn, num)
    print(f"Ước số chung lớn nhất của dãy số là: {uscln}")
    print(f"Bội số chung nhỏ nhất của dãy số là: {bscnn}")
else:
    print("Không có số tự nhiên nào được nhập.")

#bai 5
numbers = []
while True:
    n = float(input("Nhập một số (kết thúc khi nhập số 0): "))
    if n == 0:
        break
    numbers.append(n)

if numbers:
    so_luong = len(numbers)
    gia_tri_nho_nhat = min(numbers)
    gia_tri_lon_nhat = max(numbers)
    print(f"Số lượng số đã nhập: {so_luong}")
    print(f"Giá trị nhỏ nhất: {gia_tri_nho_nhat}")
    print(f"Giá trị lớn nhất: {gia_tri_lon_nhat}")
else:
    print("Không có số nào được nhập.")
