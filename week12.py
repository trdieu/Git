# Sử Dụng Bộ Dữ Liệu "HEART DISEASE"

# Tải và chuẩn bị dữ liệu
from ucimlrepo import fetch_ucirepo
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Tải dữ liệu Heart Disease
heart_disease = fetch_ucirepo(id=45)

# Chia dữ liệu thành các biến đặc trưng và biến mục tiêu
X = heart_disease.data.features
y = heart_disease.data.targets

# Tiền xử lý dữ liệu
X = X.copy()  # Tránh SettingWithCopyWarning
X.fillna(X.mean(), inplace=True)
y = y.values.ravel()  # Tránh DataConversionWarning

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Áp dụng các thuật toán phân loại
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

# Khởi tạo các mô hình phân loại
clf_dt = DecisionTreeClassifier(random_state=42)
clf_knn = KNeighborsClassifier()
clf_svm = SVC(random_state=42)

# Huấn luyện các mô hình
clf_dt.fit(X_train, y_train)
clf_knn.fit(X_train, y_train)
clf_svm.fit(X_train, y_train)

# Đánh giá hiệu suất
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Dự đoán trên tập kiểm tra
y_pred_dt = clf_dt.predict(X_test)
y_pred_knn = clf_knn.predict(X_test)
y_pred_svm = clf_svm.predict(X_test)

# Tính toán các metrics
metrics = {
    "Decision Tree": {
        "Accuracy": accuracy_score(y_test, y_pred_dt),
        "Average Precision": precision_score(y_test, y_pred_dt, average='macro', zero_division=1),
        "Average Recall": recall_score(y_test, y_pred_dt, average='macro'),
        "Average F1-Score": f1_score(y_test, y_pred_dt, average='macro')
    },
    "K-Nearest Neighbors": {
        "Accuracy": accuracy_score(y_test, y_pred_knn),
        "Average Precision": precision_score(y_test, y_pred_knn, average='macro', zero_division=1),
        "Average Recall": recall_score(y_test, y_pred_knn, average='macro'),
        "Average F1-Score": f1_score(y_test, y_pred_knn, average='macro')
    },
    "Support Vector Machine": {
        "Accuracy": accuracy_score(y_test, y_pred_svm),
        "Average Precision": precision_score(y_test, y_pred_svm, average='macro', zero_division=1),
        "Average Recall": recall_score(y_test, y_pred_svm, average='macro'),
        "Average F1-Score": f1_score(y_test, y_pred_svm, average='macro')
    }
}

# So sánh kết quả và vẽ biểu đồ
import matplotlib.pyplot as plt
import numpy as np

# Chuẩn bị dữ liệu cho biểu đồ
labels = ["Accuracy", "Average Precision", "Average Recall", "Average F1-Score"]
dt_scores = list(metrics["Decision Tree"].values())
knn_scores = list(metrics["K-Nearest Neighbors"].values())
svm_scores = list(metrics["Support Vector Machine"].values())

x = np.arange(len(labels))  # labels for groups
width = 0.2  # width of the bars

fig, ax = plt.subplots()
bars1 = ax.bar(x - width, dt_scores, width, label='Decision Tree')
bars2 = ax.bar(x, knn_scores, width, label='K-Nearest Neighbors')
bars3 = ax.bar(x + width, svm_scores, width, label='Support Vector Machine')

# Thêm một số thuộc tính cho biểu đồ
ax.set_ylabel('Scores')
ax.set_title('Comparison of Classification Algorithms')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

# Thêm nhãn cho từng thanh
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.2f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

add_labels(bars1)
add_labels(bars2)
add_labels(bars3)

fig.tight_layout()

plt.show()
