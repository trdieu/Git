#EX1
# Bước 1: Import các thư viện cần thiết
import pandas as pd

# Bước 2: Import dataset từ địa chỉ
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv'
drinks = pd.read_csv(url)

# Bước 4: Châu lục nào uống nhiều bia nhất trung bình?
beer_avg = drinks.groupby('continent')['beer_servings'].mean()
continent_max_beer = beer_avg.idxmax()
print(f"Châu lục uống nhiều bia nhất trung bình: {continent_max_beer}")

# Bước 5: In ra các thống kê về lượng tiêu thụ rượu vang cho mỗi châu lục
wine_stats = drinks.groupby('continent')['wine_servings'].describe()
print("Thống kê về lượng tiêu thụ rượu vang cho mỗi châu lục:")
print(wine_stats)

# Bước 6: In ra lượng tiêu thụ rượu trung bình cho mỗi châu lục đối với từng cột
mean_alcohol = drinks.groupby('continent').mean()
print("Lượng tiêu thụ rượu trung bình cho mỗi châu lục đối với từng cột:")
print(mean_alcohol)

# Bước 7: In ra lượng tiêu thụ rượu trung vị cho mỗi châu lục đối với từng cột
median_alcohol = drinks.groupby('continent').median()
print("Lượng tiêu thụ rượu trung vị cho mỗi châu lục đối với từng cột:")
print(median_alcohol)

# Bước 8: In ra giá trị trung bình, nhỏ nhất và lớn nhất cho lượng tiêu thụ rượu mạnh
spirit_stats = drinks.groupby('continent')['spirit_servings'].agg(['mean', 'min', 'max'])
print("Giá trị trung bình, nhỏ nhất và lớn nhất cho lượng tiêu thụ rượu mạnh:")
print(spirit_stats)

#EX2
# Bước 1: Import các thư viện cần thiết
import pandas as pd

# Bước 2: Import dataset từ địa chỉ và gán nó vào biến `users`
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'
users = pd.read_csv(url, sep='|')

# Bước 4: Tìm độ tuổi trung bình theo từng nghề nghiệp
mean_age_per_occupation = users.groupby('occupation')['age'].mean()
print("Độ tuổi trung bình theo từng nghề nghiệp:")
print(mean_age_per_occupation)

# Bước 5: Tìm tỷ lệ nam giới theo từng nghề nghiệp và sắp xếp từ cao đến thấp
# Chuyển đổi giới tính sang dạng nhị phân: 1 nếu là 'M' và 0 nếu là 'F'
users['male'] = users['gender'].apply(lambda x: 1 if x == 'M' else 0)
male_ratio_per_occupation = users.groupby('occupation')['male'].mean().sort_values(ascending=False)
print("Tỷ lệ nam giới theo từng nghề nghiệp (sắp xếp từ cao đến thấp):")
print(male_ratio_per_occupation)

# Bước 6: Tính tuổi nhỏ nhất và lớn nhất theo từng nghề nghiệp
min_max_age_per_occupation = users.groupby('occupation')['age'].agg(['min', 'max'])
print("Tuổi nhỏ nhất và lớn nhất theo từng nghề nghiệp:")
print(min_max_age_per_occupation)

# Bước 7: Tính độ tuổi trung bình theo từng kết hợp giữa nghề nghiệp và giới tính
mean_age_per_occ_gender = users.groupby(['occupation', 'gender'])['age'].mean()
print("Độ tuổi trung bình theo từng kết hợp giữa nghề nghiệp và giới tính:")
print(mean_age_per_occ_gender)

# Bước 8: Tính tỷ lệ phần trăm nam và nữ theo từng nghề nghiệp
gender_count_per_occupation = users.groupby(['occupation', 'gender']).size().unstack()
gender_percentage_per_occupation = gender_count_per_occupation.div(gender_count_per_occupation.sum(axis=1), axis=0) * 100
print("Tỷ lệ phần trăm nam và nữ theo từng nghề nghiệp:")
print(gender_percentage_per_occupation)

#EX3
# Bước 1: Import các thư viện cần thiết
import pandas as pd

# Bước 2: Tạo DataFrame với các giá trị đã cho
raw_data = {
    'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 
                 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 
                 'Scouts', 'Scouts', 'Scouts', 'Scouts'], 
    'company': ['1st', '1st', '2nd', '2nd', 
                '1st', '1st', '2nd', '2nd',
                '1st', '1st', '2nd', '2nd'], 
    'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 
             'Cooze', 'Jacon', 'Ryaner', 'Sone', 
             'Sloan', 'Piger', 'Riani', 'Ali'], 
    'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
    'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]
}

regiment = pd.DataFrame(raw_data)

# Bước 4: Tìm điểm trung bình preTestScore từ trung đoàn Nighthawks
mean_preTestScore_nighthawks = regiment[regiment['regiment'] == 'Nighthawks']['preTestScore'].mean()
print("Điểm trung bình preTestScore của trung đoàn Nighthawks:", mean_preTestScore_nighthawks)

# Bước 5: Trình bày thống kê chung theo công ty
company_stats = regiment.groupby('company').describe()
print("Thống kê chung theo công ty:")
print(company_stats)

# Bước 6: Tìm điểm trung bình của preTestScore cho từng công ty
mean_preTestScore_company = regiment.groupby('company')['preTestScore'].mean()
print("Điểm trung bình preTestScore của từng công ty:")
print(mean_preTestScore_company)

# Bước 7: Trình bày điểm trung bình preTestScores theo nhóm trung đoàn và công ty
mean_preTestScore_regiment_company = regiment.groupby(['regiment', 'company'])['preTestScore'].mean()
print("Điểm trung bình preTestScores theo nhóm trung đoàn và công ty:")
print(mean_preTestScore_regiment_company)

# Bước 8: Trình bày điểm trung bình preTestScores theo nhóm trung đoàn và công ty không có chỉ mục phân cấp
mean_preTestScore_unstacked = regiment.groupby(['regiment', 'company'])['preTestScore'].mean().unstack()
print("Điểm trung bình preTestScores theo nhóm trung đoàn và công ty không có chỉ mục phân cấp:")
print(mean_preTestScore_unstacked)

# Bước 9: Nhóm toàn bộ DataFrame theo trung đoàn và công ty
grouped_regiment_company = regiment.groupby(['regiment', 'company'])

# Bước 10: Tìm số lượng quan sát trong mỗi trung đoàn và công ty
observations_per_group = grouped_regiment_company.size()
print("Số lượng quan sát trong mỗi trung đoàn và công ty:")
print(observations_per_group)

# Bước 11: Lặp qua từng nhóm và in tên và toàn bộ dữ liệu từ trung đoàn
for name, group in grouped_regiment_company:
    print("\nName:", name)
    print(group)

