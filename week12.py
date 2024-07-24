#Sử Dụng Bộ Dữ Liệu "HEART DISEASE"


#Tải và chuẩn bị dữ liệu
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
X.fillna(X.mean(), inplace=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


#Áp dụng các thuật toán phân loại
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


#Đánh giá hiệu suất
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


from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Dự đoán trên tập kiểm tra
y_pred_dt = clf_dt.predict(X_test)
y_pred_knn = clf_knn.predict(X_test)
y_pred_svm = clf_svm.predict(X_test)

# Tính toán các metrics
metrics = {
    "Cây quyết định": {
        "Độ chính xác": accuracy_score(y_test, y_pred_dt),
        "Độ chính xác trung bình": precision_score(y_test, y_pred_dt, average='macro'),
        "Độ hồi tưởng trung bình": recall_score(y_test, y_pred_dt, average='macro'),
        "F1-Score trung bình": f1_score(y_test, y_pred_dt, average='macro')
    },
    "K-Nearest Neighbors": {
        "Độ chính xác": accuracy_score(y_test, y_pred_knn),
        "Độ chính xác trung bình": precision_score(y_test, y_pred_knn, average='macro'),
        "Độ hồi tưởng trung bình": recall_score(y_test, y_pred_knn, average='macro'),
        "F1-Score trung bình": f1_score(y_test, y_pred_knn, average='macro')
    },
    "Máy Vector hỗ trợ": {
        "Độ chính xác": accuracy_score(y_test, y_pred_svm),
        "Độ chính xác trung bình": precision_score(y_test, y_pred_svm, average='macro'),
        "Độ hồi tưởng trung bình": recall_score(y_test, y_pred_svm, average='macro'),
        "F1-Score trung bình": f1_score(y_test, y_pred_svm, average='macro')
    }
}



#So sánh kết quả và vẽ biểu đồ
import matplotlib.pyplot as plt
import numpy as np

# Chuẩn bị dữ liệu cho biểu đồ
nhan = ["Độ chính xác", "Độ chính xác trung bình", "Độ hồi tưởng trung bình", "F1-Score trung bình"]
dt_diem = list(metrics["Cây quyết định"].values())
knn_diem = list(metrics["K-Nearest Neighbors"].values())
svm_diem = list(metrics["Máy Vector hỗ trợ"].values())

x = np.arange(len(nhan))  # nhãn cho các nhóm
width = 0.2  # chiều rộng của các thanh

fig, ax = plt.subplots()
thanh1 = ax.bar(x - width, dt_diem, width, label='Cây quyết định')
thanh2 = ax.bar(x, knn_diem, width, label='K-Nearest Neighbors')
thanh3 = ax.bar(x + width, svm_diem, width, label='Máy Vector hỗ trợ')

# Thêm một số thuộc tính cho biểu đồ
ax.set_ylabel('Điểm số')
ax.set_title('So sánh các thuật toán phân loại')
ax.set_xticks(x)
ax.set_xticklabels(nhan)
ax.legend()

# Thêm nhãn cho từng thanh
def them_nhan(thanh):
    for thanh_item in thanh:
        chieu_cao = thanh_item.get_height()
        ax.annotate(f'{chieu_cao:.2f}',
                    xy=(thanh_item.get_x() + thanh_item.get_width() / 2, chieu_cao),
                    xytext=(0, 3),  # Độ dịch chuyển dọc 3 điểm
                    textcoords="offset points",
                    ha='center', va='bottom')

them_nhan(thanh1)
them_nhan(thanh2)
them_nhan(thanh3)

fig.tight_layout()

plt.show()