import mysql.connector
import sys
import json

# Import thư viện cần thiết
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Tải bộ dữ liệu Iris
iris = load_iris()
X = iris.data  # Các đặc trưng
y = iris.target  # Nhãn (class)

# Chia dữ liệu thành tập huấn luyện và kiểm tra (80% huấn luyện, 20% kiểm tra)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Chuẩn hóa dữ liệu (Standardization)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Khởi tạo mô hình Random Forest với 100 cây quyết định
rf = RandomForestClassifier(n_estimators=100, random_state=42)

# Huấn luyện mô hình
rf.fit(X_train, y_train)

# Dự đoán trên tập kiểm tra
y_pred = rf.predict(X_test)

# Tính độ chính xác (accuracy)
accuracy = accuracy_score(y_test, y_pred)


# Thiết lập kết nối đến MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",  # Thay đổi nếu bạn có user khác
    password="",  # Thay đổi nếu bạn có mật khẩu
    database="qlgv"  # Tên cơ sở dữ liệu là 'qlgv'
)

cursor = conn.cursor()



# Truy vấn dữ liệu từ bảng giangvien
cursor.execute("SELECT MaGV, HoTenGV, BoMon FROM giangvien")
rows = cursor.fetchall()

# Chuyển đổi kết quả truy vấn thành dạng JSON
result = []
for row in rows:
    result.append({
        "MaGV": row[0],
        "HoTenGV": row[1],
        "BoMon": row[2],
        "Accuracy":accuracy
    })

# Đóng kết nối
cursor.close()
conn.close()

# Trả kết quả dưới dạng JSON
print("Content-Type: application/json\n")
print(json.dumps(result))
