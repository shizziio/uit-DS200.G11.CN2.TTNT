# Lab 5.2: Tiền xử lý dữ liệu mua sắm

**Học phần:** Dữ liệu lớn (Big Data)

**Mã số sinh viên:** 26410022

**Dữ liệu:** [shopping_trends.csv](../datasets/lab5/shopping_trends.csv)

[DOCX được đặt cạnh CSV](../datasets/lab5/Lab%205_Data%20preprocessing_p2.docx) là bản sao y hệt [đề Lab 5 về xử lý văn bản PDF](../de-bai/Lab%205_Data%20preprocessing_p2.docx). Không có yêu cầu riêng cho CSV trong DOCX đó. Lab 5.2 ở đây là bài tiền xử lý dữ liệu bảng dựa trên CSV được cung cấp.

## Nội dung

1. Đọc 3.900 dòng, 19 cột; xem kiểu dữ liệu, thống kê số ô thiếu, số giá trị riêng và dữ liệu trùng.
2. Vẽ số giao dịch theo danh mục và phân bố giá trị mua hàng.
3. Bỏ `Customer ID` khỏi ma trận đặc trưng. `Discount Applied` và `Promo Code Used` giống nhau ở mọi dòng, nên giữ một cột.
4. Dùng median imputation và `StandardScaler` cho cột số; mode imputation và `OneHotEncoder` cho cột phân loại.
5. Kiểm tra ma trận kết quả chỉ chứa số và không có ô thiếu. Vì chưa có biến mục tiêu được chỉ định, bài không huấn luyện mô hình.

## Cách chạy

Từ thư mục gốc của repo:

```bash
python3 -m pip install pandas matplotlib scikit-learn
python3 lab5_2/lab5_2.py
```

Script lưu `shopping_trends_preprocessed.csv` và `shopping_trends_overview.png` trong `lab5_2/outputs/`. Notebook `lab5_2.ipynb` chạy độc lập trên Colab sau khi tệp CSV và notebook được đẩy lên GitHub; dữ liệu được đọc từ GitHub Raw.

## Kết quả kiểm tra

CSV có 0 ô thiếu, 0 dòng trùng và 0 mã khách hàng trùng. Sau tiền xử lý, ma trận có **3.900 dòng × 147 cột số**. Các bước imputation hiện không thay đổi dữ liệu vì CSV không có giá trị thiếu; chúng chuẩn bị quy trình cho dữ liệu mới có thể thiếu.
