#Sử dụng bộ dữ liệu "FOREST FIRES"

#Lấy dữ liệu và tiền xử lý
from ucimlrepo import fetch_ucirepo
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Lấy dữ liệu
forest_fires = fetch_ucirepo(id=162)
X = forest_fires.data.features
y = forest_fires.data.targets

# Hiển thị vài hàng đầu tiên của dữ liệu
print(X.head())
print(y.head())

# Chuyển đổi các thuộc tính dạng danh mục thành các biến giả
X = pd.get_dummies(X, drop_first=True)

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Chuẩn hóa dữ liệu
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


#Áp dụng các thuật toán hồi quy
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Khởi tạo các mô hình
models = {
    "Hồi quy tuyến tính": LinearRegression(),
    "Hồi quy Ridge": Ridge(alpha=1.0),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42)
}

# Huấn luyện và đánh giá các mô hình
results = {}

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    results[name] = {
        "Sai số trung bình bình phương": mean_squared_error(y_test, y_pred),
        "Sai số tuyệt đối trung bình": mean_absolute_error(y_test, y_pred),
        "R2 Score": r2_score(y_test, y_pred)
    }

# Hiển thị kết quả
for name, metrics in results.items():
    print(f"Kết quả cho {name}:")
    for metric, value in metrics.items():
        print(f"{metric}: {value}")
    print()


#Vẽ biểu đồ so sánh
import matplotlib.pyplot as plt
import numpy as np

# Chuẩn bị dữ liệu để vẽ
metrics_names = ["Sai số trung bình bình phương", "Sai số tuyệt đối trung bình", "R2 Score"]
metrics_values = {metric: [results[model][metric] for model in models] for metric in metrics_names}

x = np.arange(len(models))
width = 0.25

fig, ax = plt.subplots(1, 3, figsize=(18, 6))

for i, metric in enumerate(metrics_names):
    ax[i].bar(x - width, metrics_values[metric], width, label=metric)
    ax[i].set_title(metric)
    ax[i].set_xticks(x)
    ax[i].set_xticklabels(models.keys())
    ax[i].legend()

plt.tight_layout()
plt.show()
