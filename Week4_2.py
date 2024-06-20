#bai 1
def print_first_5_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for i in range(min(5, len(lines))):
                print(lines[i], end='')
    except FileNotFoundError:
        print("Lỗi: Không tìm thấy file.")

# Đường dẫn đến file cần đọc
file_path = 'dieu.txt'

# Gọi hàm để in ra 5 dòng đầu tiên
print_first_5_lines(file_path)

#bai 2
def print_last_5_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            # In ra 5 dòng cuối hoặc toàn bộ nội dung nếu không đủ 5 dòng
            for line in lines[-5:]:
                print(line, end='')
    except FileNotFoundError:
        print("Lỗi: Không tìm thấy file.")

# Đường dẫn đến file cần đọc
file_path = 'dieu.txt'

# Gọi hàm để in ra 5 dòng cuối cùng
print_last_5_lines(file_path)

#bai 3
def print_longest_line(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            longest_line = max(lines, key=len)
            print("Dòng dài nhất trong file là:")
            print(longest_line)
    except FileNotFoundError:
        print("Lỗi: Không tìm thấy file.")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")

# Đường dẫn đến file cần đọc
file_path = 'dieu.txt'

# Gọi hàm để in ra dòng dài nhất
print_longest_line(file_path)

#bai 4
def print_longest_word(file_path):
    try:
        with open(file_path, 'r') as file:
            words = file.read().split()
            longest_word = max(words, key=len)
            print("Từ dài nhất trong file là:")
            print(longest_word)
    except FileNotFoundError:
        print("Lỗi: Không tìm thấy file.")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")

# Đường dẫn đến file cần đọc
file_path = 'dieu.txt'

# Gọi hàm để in ra từ dài nhất
print_longest_word(file_path)

#bai 5
def count_letters(file_path):
    from collections import Counter
    import string

    try:
        with open(file_path, 'r') as file:
            text = file.read().lower()  # Chuyển toàn bộ văn bản thành chữ thường
            letters = [char for char in text if char in string.ascii_lowercase]  # Lọc ra các chữ cái
            letter_counts = Counter(letters)
            
            print("Thống kê các chữ cái trong file:")
            for letter, count in letter_counts.items():
                print(f"{letter}: {count}")
    except FileNotFoundError:
        print("Lỗi: Không tìm thấy file.")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")

# Đường dẫn đến file cần đọc
file_path = 'dieu.txt'

# Gọi hàm để thống kê và in ra số lần xuất hiện của các chữ cái
count_letters(file_path)

#bai 6
from collections import Counter

def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read().lower()  # Chuyển toàn bộ văn bản thành chữ thường
            words = text.split()  # Tách văn bản thành các từ
            word_counts = Counter(words)  # Đếm tần suất xuất hiện của các từ
            sorted_word_counts = word_counts.most_common()  # Sắp xếp theo thứ tự giảm dần của số lần xuất hiện
            
            print("Tần suất xuất hiện của các từ trong file:")
            for word, count in sorted_word_counts:
                print(f"{word}: {count}")
    except FileNotFoundError:
        print("Lỗi: Không tìm thấy file.")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")

# Đường dẫn đến file cần đọc
file_path = 'dieu.txt'

# Gọi hàm để thống kê và in ra tần suất xuất hiện của các từ
count_words(file_path)

#bai 7
# Đọc nội dung từ tập tin abc.txt
with open('abc.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# Chuyển nội dung sang chữ in hoa
upper_content = content.upper()

# Ghi nội dung đã chuyển sang chữ in hoa vào tập tin xyz.txt
with open('xyz.txt', 'w', encoding='utf-8') as file:
    file.write(upper_content)

#bai 8
import re

# Đọc nội dung từ tập tin abc.txt
with open('abc.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# Lọc các số trong nội dung đọc được
numbers = re.findall(r'\d+', content)

# Ghi các số vào tập tin number.txt, mỗi số trên một dòng
with open('number.txt', 'w', encoding='utf-8') as file:
    for number in numbers:
        file.write(number + '\n')

#bai 9
# Nhập tên của hai tập tin văn bản
file1 = input("Nhập tên tập tin thứ nhất: ")
file2 = input("Nhập tên tập tin thứ hai: ")

# Đọc nội dung của tập tin thứ nhất
with open(file1, 'r', encoding='utf-8') as f1:
    content1 = f1.read()

# Đọc nội dung của tập tin thứ hai
with open(file2, 'r', encoding='utf-8') as f2:
    content2 = f2.read()

# So sánh nội dung của hai tập tin
if content1 == content2:
    print("Nội dung của hai tập tin giống nhau.")
else:
    print("Nội dung của hai tập tin khác nhau.")

#bai 10
import os
import hashlib

def hash_file(filename):
    """Trả về hash của nội dung tập tin."""
    hasher = hashlib.md5()
    with open(filename, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

# Lấy danh sách các tập tin trong thư mục hiện tại
files = [f for f in os.listdir() if os.path.isfile(f)]

# Tạo từ điển để lưu hash và danh sách các tập tin tương ứng
file_hashes = {}

for filename in files:
    file_hash = hash_file(filename)
    if file_hash in file_hashes:
        file_hashes[file_hash].append(filename)
    else:
        file_hashes[file_hash] = [filename]

# In ra các nhóm tập tin có cùng nội dung
group_number = 1
for file_list in file_hashes.values():
    if len(file_list) > 1:
        print(f"Nhóm {group_number}: {', '.join(file_list)}")
        group_number += 1

#bai 11
# Nhập tên tệp từ người dùng
file_name = input("Nhập tên tệp: ")

try:
    # Mở tệp ở chế độ nhị phân
    with open(file_name, 'rb') as file:
        # Đọc 10 byte đầu tiên của tệp
        header = file.read(10)
        
        # Kiểm tra 4 byte từ vị trí thứ 6 đến thứ 9
        if header[6:10] == b'JFIF':
            print("Đây có thể là tệp ảnh jpg.")
        else:
            print("Đây không phải là tệp ảnh jpg.")
except FileNotFoundError:
    print("Tệp không tồn tại.")
except Exception as e:
    print(f"Có lỗi xảy ra: {e}")

#bai 12
import struct

# Nhập tên tệp từ người dùng
file_name = input("Nhập tên tệp: ")

try:
    # Mở tệp ở chế độ nhị phân
    with open(file_name, 'rb') as file:
        # Đọc 26 byte đầu tiên của tệp
        header = file.read(26)
        
        # Kiểm tra 2 byte đầu có phải là "BM" không
        if header[:2] == b'BM':
            # Lấy số dòng (chiều cao) từ vị trí 18-21 (4 byte)
            height = struct.unpack('<I', header[18:22])[0]
            # Lấy số cột (chiều ngang) từ vị trí 22-25 (4 byte)
            width = struct.unpack('<I', header[22:26])[0]
            print(f"Đây là tệp ảnh bitmap (BMP). Kích thước: {height} x {width} (dòng x cột).")
        else:
            print("Đây không phải là tệp ảnh bitmap (BMP).")
except FileNotFoundError:
    print("Tệp không tồn tại.")
except Exception as e:
    print(f"Có lỗi xảy ra: {e}")
