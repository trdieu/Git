#bai 1
try:
    # Nhập hai số nguyên từ người dùng
    a = int(input("Nhập số nguyên a: "))
    b = int(input("Nhập số nguyên b: "))

    # Tính giá trị phân số a/b
    result = a / b

    # In ra kết quả
    print(f"Giá trị phân số {a}/{b} là: {result}")

except ValueError:
    print("Lỗi: Bạn đã nhập không phải số nguyên.")
except ZeroDivisionError:
    print("Lỗi: Bạn không thể chia cho số 0.")

#bai 2
def is_triangle(a, b, c):
    # Kiểm tra xem a, b, c có thể là cạnh của một tam giác hay không
    return a + b > c and a + c > b and b + c > a

try:
    # Nhập độ dài 3 cạnh từ người dùng
    a = float(input("Nhập độ dài cạnh a: "))
    b = float(input("Nhập độ dài cạnh b: "))
    c = float(input("Nhập độ dài cạnh c: "))

    # Xử lý các điều kiện
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Độ dài cạnh phải là số dương và khác 0.")
    elif not is_triangle(a, b, c):
        raise ValueError("Độ dài a, b, c không thể tạo thành một tam giác.")

    # Nếu không có lỗi, thông báo là là tam giác hợp lệ
    print("Ba cạnh a, b, c tạo thành một tam giác hợp lệ.")

except ValueError as ve:
    print(f"Lỗi: {ve}")
except Exception as e:
    print(f"Lỗi không xác định: {e}")

#bai 3
try:
    count_even_numbers = 0
    previous_number = None
    while True:
        num = input("Nhập một số nguyên dương (nhập 0 để kết thúc): ")
        
        if num.isdigit():
            num = int(num)
            if num < 0:
                raise ValueError("Lỗi số âm!!!")
            elif num == 0:
                break
            elif previous_number == num:
                raise ValueError("Lỗi nhập lặp")
            elif num % 2 == 0:
                count_even_numbers += 1
                if count_even_numbers == 5:
                    raise ValueError("Lỗi nhập chẵn")
            else:
                count_even_numbers = 0
            
            previous_number = num
        else:
            raise ValueError("Lỗi nhập số")

except ValueError as ve:
    print(f"Lỗi: {ve}")
