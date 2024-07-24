import pandas as pd
from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt

# 1. Lấy dữ liệu và tiền xử lý

# Lấy dữ liệu từ UCI Machine Learning Repository
forest_fires = fetch_ucirepo(id=162)
X = forest_fires.data.features
y = forest_fires.data.targets

# Chuyển đổi các đặc trưng phân loại thành số
X = pd.get_dummies(X, columns=['month', 'day'], drop_first=True)

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Chuẩn hóa dữ liệu
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 2. Áp dụng các thuật toán hồi quy

# Định nghĩa pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('regressor', LinearRegression())
])

# Định nghĩa các tham số cần tinh chỉnh cho GridSearchCV
parameters = {'regressor__fit_intercept': [True, False]}
grid_search = GridSearchCV(pipeline, parameters, cv=5, scoring='neg_mean_squared_error')

# Huấn luyện mô hình với GridSearchCV
grid_search.fit(X_train, y_train)

# Lấy mô hình tốt nhất
best_model = grid_search.best_estimator_

# Dự đoán các giá trị trên tập kiểm tra
y_pred = best_model.predict(X_test_scaled)

# Tính toán các chỉ số hiệu suất
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
mae = mean_absolute_error(y_test, y_pred)
mape = (abs((y_test - y_pred) / y_test)).mean() * 100

print(f"MSE: {mse}")
print(f"RMSE: {rmse}")
print(f"MAE: {mae}")
print(f"MAPE: {mape}")

# 3. Vẽ biểu đồ so sánh

# Vẽ đồ thị so sánh giá trị thực tế và giá trị dự đoán
plt.figure(figsize=(10, 5))
plt.plot(y_test.values, label='Giá trị thực tế', color='blue')
plt.plot(y_pred, label='Giá trị dự đoán', color='red')
plt.xlabel('Chỉ số')
plt.ylabel('Diện tích')
plt.title('So sánh giá trị thực tế và giá trị dự đoán')
plt.legend()
plt.show()
