# LAB 2: LÀM VIỆC VỚI DỮ LIỆU BỊ THIẾU TRONG THƯ VIỆN PANDAS (MISSING DATA)
**Mã số SV**: 26410022  
**Học phần**: Dữ liệu lớn (Big Data)

---

## 1. Cấu trúc thư mục `lab2`

- `../datasets/lab2/employees.csv`: Bộ dữ liệu nhân viên thực tế dùng cho thực hành (1000 dòng x 8 cột) chứa các giá trị khuyết thiếu.
- `lab2.py`: Script Python thực hiện tuần tự và hoàn chỉnh toàn bộ các nội dung của bài Lab 2.
- `lab2.ipynb`: Jupyter Notebook tương tác từng bước, có đầy đủ phần lý thuyết (MCAR, MAR, MNAR), code mẫu theo yêu cầu và toàn bộ kết quả output đã được execute sẵn.
- `README.md`: Hướng dẫn cấu trúc bài làm và cách thực thi.

---

## 2. Tóm tắt nội dung bài thực hành

1. **Phát hiện dữ liệu bị thiếu**: Sử dụng hàm `isnull()` / `isna()` và `notnull()` trên DataFrame tạo từ dictionary.
2. **Làm việc với dataset thực tế (`employees.csv`)**: Lọc và trích xuất các bản ghi có thuộc tính `Gender` bị thiếu (`NaN`) bằng boolean indexing.
3. **Điền và xử lý giá trị còn thiếu**:
   - `fillna(0)`: Điền giá trị hằng số cố định vào ô trống.
   - `fillna(method='pad')` / `ffill()`: Điền giá trị khuyết bằng giá trị hợp lệ liền trước.
   - `replace(to_replace=np.nan, value=-88)`: Thay thế toàn bộ giá trị `NaN` bằng một giá trị đại diện.
   - `interpolate(method='linear', limit_direction='forward')`: Ước lượng và điền giá trị khuyết bằng phương pháp nội suy tuyến tính.

---

## 3. Cách chạy

### Chạy bằng script Python:
```bash
python3 lab2/lab2.py
```

### Chạy bằng Jupyter Notebook:
Mở file `lab2/lab2.ipynb` trên VS Code hoặc Jupyter Lab và thực thi tuần tự các cell.

Dữ liệu đầu vào của bài được đọc từ GitHub Raw khi chạy trên Colab; xem README ở thư mục gốc để biết URL.
