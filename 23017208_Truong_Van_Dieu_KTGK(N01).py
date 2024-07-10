# 1. Import các thư viện cần thiết
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Thiết lập kiểu cho các biểu đồ
sns.set(style="whitegrid")


# 2. Đọc dữ liệu từ file này address và gán tên biến là df. Đồng thời thiết lập tên các features dựa trên thông tin đã cho ở đầu bài.
address = 'https://raw.githubusercontent.com/thieu1995/csv-files/main/data/pandas/adult.data'
column_names = ["age", "workclass", "fnlwgt", "education", "education-num", "marital-status", 
                "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss", 
                "hours-per-week", "native-country", "salary"]
df = pd.read_csv(address, names=column_names)


# 3. In ra giá trị 15 hàng dữ liệu đầu tiên của bảng
print("15 hàng dữ liệu đầu tiên:")
print(df.head(15))


# 4. In ra tất cả các giá trị unique của tất cả các cột trong bảng
for column in df.columns:
    unique_values = df[column].unique()
    print(f"Giá trị unique trong cột {column}: {unique_values}")


# 5. Tạo biểu đồ histogram của cột hours-per-week (số giờ làm trong 1 tuần)
plt.figure(figsize=(10, 6))
sns.histplot(df['hours-per-week'], bins=20, kde=True)
plt.title('Biểu đồ Histogram của số giờ làm việc trong 1 tuần')
plt.xlabel('Số giờ làm việc trong 1 tuần')
plt.ylabel('Tần suất')
plt.show()


# 6. Tạo biểu đồ histogram của cột hours-per-week của những người có số năm giáo dục (education-num) >= 9.
plt.figure(figsize=(10, 6))
sns.histplot(df[df['education-num'] >= 9]['hours-per-week'], bins=20, kde=True)
plt.title('Biểu đồ Histogram của số giờ làm việc trong 1 tuần (Số năm giáo dục >= 9)')
plt.xlabel('Số giờ làm việc trong 1 tuần')
plt.ylabel('Tần suất')
plt.show()


# 7. Tạo biểu đồ pie chart thể hiện phần trăm của cột race và sex
race_sex = df.groupby(['race', 'sex']).size().unstack()
race_sex.plot(kind='pie', subplots=True, autopct='%1.1f%%', figsize=(14, 10))
plt.title('Phần trăm của Chủng tộc và Giới tính')
plt.show()


# 8. Tạo biểu đồ pie chart cho cột workclass
workclass_counts = df['workclass'].value_counts()
plt.figure(figsize=(10, 6))
workclass_counts.plot.pie(autopct='%1.1f%%')
plt.title('Phần trăm của Workclass')
plt.ylabel('')
plt.show()


# 9. Tạo biểu đồ scatter chart cho cột education-num và cột age
plt.figure(figsize=(10, 6))
sns.scatterplot(x='education-num', y='age', data=df)
plt.title('Biểu đồ Scatter của Số năm giáo dục và Tuổi')
plt.xlabel('Số năm giáo dục')
plt.ylabel('Tuổi')
plt.show()


# 10. Tạo biểu đồ scatter chart cho cột age và cột hours-per-week
plt.figure(figsize=(10, 6))
sns.scatterplot(x='age', y='hours-per-week', data=df)
plt.title('Biểu đồ Scatter của Tuổi và Số giờ làm việc trong 1 tuần')
plt.xlabel('Tuổi')
plt.ylabel('Số giờ làm việc trong 1 tuần')
plt.show()


# 11. Tạo biểu đồ box plot cho cột race và cột education-num
plt.figure(figsize=(12, 6))
sns.boxplot(x='race', y='education-num', data=df)
plt.title('Biểu đồ Box Plot của Chủng tộc và Số năm giáo dục')
plt.xlabel('Chủng tộc')
plt.ylabel('Số năm giáo dục')
plt.show()


# 12. Tạo biểu đồ box plot cho cột workclass và cột hours-per-week
plt.figure(figsize=(12, 6))
sns.boxplot(x='workclass', y='hours-per-week', data=df)
plt.title('Biểu đồ Box Plot của Workclass và Số giờ làm việc trong 1 tuần')
plt.xlabel('Workclass')
plt.ylabel('Số giờ làm việc trong 1 tuần')
plt.show()


# 13. In ra 5 hàng cuối cùng của bảng dữ liệu
print("5 hàng cuối cùng của bảng dữ liệu:")
print(df.tail(5))


# 14. Hiển thị các giá trị thống kê đối với các features dạng số và cho biết giá trị mean của capital-gain là bao nhiêu?
print("Giá trị thống kê đối với các features dạng số:")
print(df.describe())
mean_capital_gain = df['capital-gain'].mean()
print(f"Giá trị trung bình của capital-gain: {mean_capital_gain}")


# 15. Độ tuổi trung bình của phụ nữ là bao nhiêu?
mean_age_women = df[df['sex'] == 'Female']['age'].mean()
print(f"Độ tuổi trung bình của phụ nữ: {mean_age_women}")


# 16. Phần trăm dân số người Đức là bao nhiêu (cột native-country)?
total_population = len(df)
german_population = len(df[df['native-country'] == 'Germany'])
german_percentage = (german_population / total_population) * 100
print(f"Phần trăm dân số người Đức: {german_percentage:.2f}%")


# 17. Độ lệch chuẩn và giá trị trung bình của độ tuổi đối với những người kiếm được hơn 50K mỗi năm và những người kiếm được ít hơn 50K mỗi năm là bao nhiêu?
mean_std_over_50k = df[df['salary'] == '>50K']['age'].agg(['mean', 'std'])
mean_std_under_50k = df[df['salary'] == '<=50K']['age'].agg(['mean', 'std'])
print(f"Giá trị trung bình và độ lệch chuẩn của độ tuổi đối với những người kiếm được >50K: {mean_std_over_50k}")
print(f"Giá trị trung bình và độ lệch chuẩn của độ tuổi đối với những người kiếm được <=50K: {mean_std_under_50k}")


# 18. Có đúng là những người kiếm được hơn 50K đều có trình độ học vấn ít nhất là high school?
high_education = ['Bachelors', 'Prof-school', 'Assoc-acdm', 'Assoc-voc', 'Masters', 'Doctorate']
high_edu_people = df[df['salary'] == '>50K']['education'].isin(high_education).all()
print(f"Những người kiếm được >50K có trình độ học vấn ít nhất là high school? {high_edu_people}")


# 19. Hiển thị thống kê độ tuổi cho từng chủng tộc và từng giới tính. Sử dụng groupby() describe(). Tìm độ tuổi tối đa của nam giới thuộc chủng tộc Amer-Indian-Eskimo.
age_stats = df.groupby(['race', 'sex'])['age'].describe()
print("Thống kê độ tuổi cho từng chủng tộc và từng giới tính:")
print(age_stats)
max_age_amerindian_male = df[(df['race'] == 'Amer-Indian-Eskimo') & (df['sex'] == 'Male')]['age'].max()
print(f"Độ tuổi tối đa của nam giới thuộc chủng tộc Amer-Indian-Eskimo: {max_age_amerindian_male}")


# 20. Tỉ lệ người married hay single men chiếm nhiều hơn trong số những người kiếm được >50K?
married_statuses = ['Married-civ-spouse', 'Married-spouse-absent', 'Married-AF-spouse']
married_men = df[(df['sex'] == 'Male') & (df['marital-status'].isin(married_statuses)) & (df['salary'] == '>50K')]
single_men = df[(df['sex'] == 'Male') & (~df['marital-status'].isin(married_statuses)) & (df['salary'] == '>50K')]
print(f"Số người đàn ông đã kết hôn kiếm được >50K: {len(married_men)}")
print(f"Số người đàn ông độc thân kiếm được >50K: {len(single_men)}")


# 21. Số giờ tối đa một người làm việc mỗi tuần là bao nhiêu? Có bao nhiêu người làm việc với số giờ như vậy và tỷ lệ những người kiếm được nhiều (>50K) trong số đó là bao nhiêu?
max_hours = df['hours-per-week'].max()
people_max_hours = df[df['hours-per-week'] == max_hours]
number_people_max_hours = len(people_max_hours)
earning_more_50k = len(people_max_hours[people_max_hours['salary'] == '>50K'])
percentage_earning_more_50k = (earning_more_50k / number_people_max_hours) * 100
print(f"Số giờ tối đa một người làm việc mỗi tuần: {max_hours}")
print(f"Số người làm việc với số giờ tối đa: {number_people_max_hours}")
print(f"Tỷ lệ những người kiếm được >50K trong số đó: {percentage_earning_more_50k:.2f}%")


# 22. Tính thời gian làm việc trung bình của những người kiếm được ít và nhiều cho mỗi quốc gia. Kết quả cho đất nước Nhật Bản.
mean_hours_per_week = df.groupby(['native-country', 'salary'])['hours-per-week'].mean().unstack()
print("Thời gian làm việc trung bình của những người kiếm được ít và nhiều cho mỗi quốc gia:")
print(mean_hours_per_week)

if 'Japan' in mean_hours_per_week.index:
    mean_hours_japan = mean_hours_per_week.loc['Japan']
    print(f"Thời gian làm việc trung bình ở Nhật Bản cho <=50K: {mean_hours_japan['<=50K']:.2f}")
    print(f"Thời gian làm việc trung bình ở Nhật Bản cho >50K: {mean_hours_japan['>50K']:.2f}")
else:
    print("Nhật Bản không có trong dataset.")


# 23. Số người da trắng kiếm được số tiền >50k ở nước Mỹ chiếm bao nhiêu phần trăm. Câu hỏi tương tự với người da đen.
total_white_us = df[(df['race'] == 'White') & (df['native-country'] == 'United-States')]
total_black_us = df[(df['race'] == 'Black') & (df['native-country'] == 'United-States')]

white_earning_more_50k = len(total_white_us[total_white_us['salary'] == '>50K'])
black_earning_more_50k = len(total_black_us[total_black_us['salary'] == '>50K'])

if len(total_white_us) > 0:
    percentage_white_earning_more_50k = (white_earning_more_50k / len(total_white_us)) * 100
else:
    percentage_white_earning_more_50k = 0

if len(total_black_us) > 0:
    percentage_black_earning_more_50k = (black_earning_more_50k / len(total_black_us)) * 100
else:
    percentage_black_earning_more_50k = 0

print(f"Tỷ lệ người da trắng kiếm được >50K ở Mỹ: {percentage_white_earning_more_50k:.2f}%")
print(f"Tỷ lệ người da đen kiếm được >50K ở Mỹ: {percentage_black_earning_more_50k:.2f}%")
