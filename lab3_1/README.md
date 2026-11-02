# Lab 3.1: Hồi quy tuyến tính đơn giản

**Học phần:** Dữ liệu lớn (Big Data)
**Mã số sinh viên:** 26410022
**Đề bài:** [LAB-3.1.pdf](../de-bai/LAB-3.1.pdf)

## Nội dung

Dự đoán `Salary` từ một biến `YearsExperience` bằng mô hình `LinearRegression` theo phương trình `Salary = b0 + b1 × YearsExperience`. Bài thực hành gồm ba bước trong đề: tải dữ liệu, trực quan hóa và huấn luyện mô hình. Dữ liệu được chia 80% train và 20% test với `random_state=42`.

- `../datasets/lab3_1/Salary_Data.csv`: 30 quan sát, hai cột `YearsExperience` và `Salary`. [Nguồn dữ liệu](https://github.com/pravinknr/DataScience_R_Codes/blob/master/2.%20Implemetation%20of%20the%20Algorithms%20on%20Datasets/Linear%20Regression/Simple%20Linear%20Regression/Salary%20Data/Salary_Data.csv), khớp với dữ liệu trong đề.
- `lab3_1.ipynb`: notebook có giải thích, bảng dữ liệu, biểu đồ, dự đoán và R²; đọc CSV cục bộ khi có, hoặc GitHub Raw trên Colab.
- `lab3_1.py`: script thực hiện cùng bài và lưu 5 biểu đồ vào `lab3_1/outputs/`.

## Cách chạy

Tại thư mục gốc của repo:

```bash
python3 -m pip install pandas matplotlib seaborn scikit-learn
python3 lab3_1/lab3_1.py
```

Mở `lab3_1.ipynb` trong Jupyter/VS Code hoặc bằng liên kết Colab ở README gốc, rồi chạy các cell từ trên xuống. Trên Colab, notebook tải CSV bằng GitHub Raw sau khi các tệp mới được đẩy lên nhánh `main`.

## Kết quả mong đợi

Với bộ dữ liệu trên và phép chia của đề: 24 dòng train, 6 dòng test; R² train khoảng **0.96454**, R² test khoảng **0.90245**. R² là hệ số xác định của hồi quy, không phải tỷ lệ dự đoán chính xác từng mức lương. Biểu đồ train/test thể hiện điểm dữ liệu thực tế và đường hồi quy đã học từ tập train.
