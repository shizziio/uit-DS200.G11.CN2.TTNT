# LAB 3: LÀM SẠCH DỮ LIỆU TRONG PANDAS (DATA CLEANING)
**Mã số SV**: 26410022  
**Học phần**: Dữ liệu lớn (Big Data)

---

## 1. Cấu trúc thư mục `lab3`

- `../datasets/lab3/property_data.csv`: Bộ dữ liệu bất động sản dùng cho phần bài tập (các cột: PID, ST_NUM, ST_NAME, OWN_OCCUPIED, NUM_BEDROOMS, NUM_BATH, SQ_FT).
- `../datasets/lab3/sample_data.csv`: Bộ dữ liệu nhân viên / địa chỉ dùng để tái hiện và thực hành toàn bộ các lệnh biến đổi tên cột trong phần hướng dẫn Google Colab.
- `lab3.py`: Script Python thực hiện tuần tự, tự động và đầy đủ tất cả các nội dung từ Phần I, II (Thực hành thao tác cột) đến Phần III (Giải quyết toàn bộ bài tập về nhà).
- `lab3.ipynb`: Jupyter Notebook hoàn chỉnh, có giải thích lý thuyết chi tiết, các bước code rõ ràng và toàn bộ kết quả output đã được execute sẵn.
- `README.md`: Báo cáo hướng dẫn chi tiết nội dung, kết quả thực hiện và cách chạy bài lab.

---

## 2. Tóm tắt nội dung bài thực hành

### Phần 1 & 2: Thao tác trên cột dữ liệu (Column & Header Manipulations)
1. **Chuẩn hóa chữ hoa / chữ thường**:
   - `df.columns.str.lower()`: Chuyển toàn bộ tiêu đề cột sang chữ thường.
   - `df.columns.str.upper()`: Chuyển toàn bộ tiêu đề cột sang chữ in hoa.
   - `df.columns.str.title()`: Viết hoa chữ cái đầu tiên của từng từ.
2. **Chuẩn hóa khoảng trắng**:
   - `df.columns.str.replace(' ', '_')`: Thay thế khoảng trắng bằng ký tự gạch dưới để chuẩn hóa naming convention.
3. **Đổi tên cột**:
   - Dùng `df.rename(columns={'Age': 'Date of Birth'})`.
   - Gán trực tiếp qua chỉ mục `df.columns.values[7] = 'Email Address'`.
4. **Lọc và chọn cột**:
   - Chọn tất cả cột trừ một cột điều kiện: `df.columns[df.columns != 'SALARY']` hoặc phủ định `~df.columns.isin(['SALARY'])`.
   - Chọn cột theo từ khóa: `df.filter(like='STREET').columns`.
   - Chọn cột kết thúc bằng cụm từ: `df.loc[:, df.columns.str.endswith('name')].columns` hoặc regex `df.filter(regex='(?i)name$', axis=1).columns`.
   - Trích xuất nhóm cột theo slice chỉ mục: `df.columns.values[0:4]`.

---

### Phần 3: Giải quyết bài tập về nhà (`property_data.csv`)
1. **2.1. Đọc tệp CSV vào Dataframe**:
   - Nhận diện các giá trị khuyết đặc thù trong thực tế bằng `pd.read_csv('https://raw.githubusercontent.com/shizziio/uit-DS200.G11.CN2.TTNT/main/datasets/lab3/property_data.csv', na_values=['n/a', 'na', '--'])`.
2. **2.2. Tìm dữ liệu bị thiếu trong Dataframe**:
   - Dùng `df.isnull()` và thống kê số lượng ô khuyết theo cột với `df.isnull().sum()`.
3. **2.3. Xem cột `NUM_BEDROOMS` và tìm giá trị `NaN`**:
   - Trích xuất cột `df['NUM_BEDROOMS']` và lọc các dòng bị khuyết: `df[df['NUM_BEDROOMS'].isnull()]` (tìm thấy 3 dòng có giá trị NaN tại index 2, 5, 8).
4. **2.4. Tính tổng giá trị còn thiếu trong Dataframe**:
   - Sử dụng `df.isnull().sum().sum()` -> Kết quả: có tổng cộng **10 giá trị thiếu**.
5. **2.5a. Điền giá trị 126 vào ô bị thiếu trong cột `ST_NUM`**:
   - Thực hiện điền: `df['ST_NUM'] = df['ST_NUM'].fillna(126)`.
6. **2.5b. Thay thế missing values trong cột `NUM_BEDROOMS` bằng trung vị (median)**:
   - Tính `median = df['NUM_BEDROOMS'].median()` -> Kết quả: `2.5`.
   - Điền giá trị: `df['NUM_BEDROOMS'] = df['NUM_BEDROOMS'].fillna(median)`.

---

## 3. Cách chạy

### Chạy bằng script Python:
```bash
python3 lab3/lab3.py
```

### Chạy bằng Jupyter Notebook:
Mở file `lab3/lab3.ipynb` trên VS Code hoặc Jupyter Lab và thực thi tuần tự các cell.

Dữ liệu đầu vào của bài được đọc từ GitHub Raw khi chạy trên Colab; xem README ở thư mục gốc để biết URL.
