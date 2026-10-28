"""
LAB 3: LÀM SẠCH DỮ LIỆU (DATA CLEANING)
Học phần: Dữ liệu lớn (Big Data)
Mã số sinh viên: 26410022
"""

import pandas as pd
import numpy as np

DATASET_BASE_URL = "https://raw.githubusercontent.com/shizziio/uit-DS200.G11.CN2.TTNT/main/datasets/lab3"

def main():
    print("=" * 70)
    print("PHẦN 1 & 2: THỰC HÀNH CÁC THAO TÁC LÀM SẠCH VÀ BIẾN ĐỔI TÊN CỘT")
    print("=" * 70)

    # 1. Đọc dữ liệu mẫu từ sample_data.csv (tái hiện tutorial trên Google Colab)
    sample_path = f"{DATASET_BASE_URL}/sample_data.csv"
    df_sample = pd.read_csv(sample_path)
    print("\n[+] Dữ liệu mẫu ban đầu (df_sample.head()):")
    print(df_sample.head())

    # 2. Thay đổi tiêu đề các cột thành chữ thường (df.columns.str.lower())
    lower_cols = df_sample.columns.str.lower()
    print("\n[+] Tiêu đề cột thành chữ thường:")
    print(lower_cols)

    # 3. Thay đổi tiêu đề các cột thành chữ in hoa (df.columns.str.upper())
    upper_cols = df_sample.columns.str.upper()
    print("\n[+] Tiêu đề cột thành chữ in hoa:")
    print(upper_cols)

    # 4. Ký tự đầu in hoa (df.columns.str.title())
    title_cols = df_sample.columns.str.title()
    print("\n[+] Ký tự đầu in hoa:")
    print(title_cols)

    # 5. Thay thế khoảng trắng bằng dấu gạch dưới (df.columns.str.replace(' ', '_'))
    underscore_cols = df_sample.columns.str.replace(' ', '_')
    print("\n[+] Thay khoảng trắng bằng dấu gạch dưới (_):")
    print(underscore_cols)

    # 6. Đổi tên cột: 'Age' thành 'Date of Birth'
    df_renamed = df_sample.rename(columns={'Age': 'Date of Birth'})
    print("\n[+] Đổi tên cột 'Age' -> 'Date of Birth':")
    print(df_renamed.head())

    # 7. Đổi tên cột bằng chỉ mục giá trị (df.columns.values[7] = 'Email Address')
    df_renamed_copy = df_renamed.copy()
    df_renamed_copy.columns.values[7] = 'Email Address'
    print("\n[+] Danh sách cột sau khi gán df.columns.values[7] = 'Email Address':")
    print(df_renamed_copy.columns)

    # 8. Chọn tất cả các cột trừ một cột điều kiện
    cols_without_salary = df_renamed_copy.columns[df_renamed_copy.columns != 'SALARY']
    print("\n[+] Lấy tất cả cột trừ 'SALARY' (phép so sánh !=):")
    print(cols_without_salary)

    cols_isin_salary = df_renamed_copy.loc[:, ~df_renamed_copy.columns.isin(['SALARY'])].columns
    print("[+] Lấy tất cả cột trừ 'SALARY' (dùng phủ định ~isin):")
    print(cols_isin_salary)

    # 9. Chọn tên cột bắt đầu bằng cụm từ (df.filter(like='STREET').columns)
    filter_street = df_renamed_copy.filter(like='STREET').columns
    print("\n[+] Lọc tên cột chứa 'STREET':")
    print(filter_street)

    # 10. Chọn tên cột có đuôi kết thúc cụ thể (endswith hoặc regex)
    endswith_name = df_renamed_copy.loc[:, df_renamed_copy.columns.str.endswith('name') | df_renamed_copy.columns.str.endswith('Name')].columns
    print("\n[+] Cột kết thúc bằng 'name' hoặc 'Name' (endswith):")
    print(endswith_name)

    regex_name = df_renamed_copy.filter(regex='(?i)name$', axis=1).columns
    print("[+] Cột kết thúc bằng 'name' (filter regex):")
    print(regex_name)

    # 11. Chọn một nhóm tên cột theo khoảng slice
    slice_cols = df_renamed_copy.columns.values[0:4]
    print("\n[+] Nhóm tên cột từ vị trí 0 đến 3 (df.columns.values[0:4]):")
    print(slice_cols)

    print("\n" + "=" * 70)
    print("PHẦN 3: BÀI TẬP VỀ NHÀ (THỰC HIỆN TRÊN BỘ DỮ LIỆU PROPERTY_DATA.CSV)")
    print("=" * 70)

    prop_path = f"{DATASET_BASE_URL}/property_data.csv"

    # 2.1. Đọc tệp csv vào Dataframe
    print("\n--- 2.1 Đọc tệp csv vào Dataframe ---")
    # Định nghĩa các giá trị khuyết thiếu đặc thù trong thực tế của dataset
    missing_value_formats = ["n/a", "na", "--"]
    df_raw = pd.read_csv(prop_path)
    df_prop = pd.read_csv(prop_path, na_values=missing_value_formats)
    print("[+] Dữ liệu đọc cơ bản (Standard read):")
    print(df_raw)
    print("\n[+] Dữ liệu đọc có xử lý các định dạng khuyết lạ (na_values=['n/a', 'na', '--']):")
    print(df_prop)

    # 2.2. Tìm trong Dataframe những dữ liệu bị thiếu
    print("\n--- 2.2 Tìm trong Dataframe những dữ liệu bị thiếu ---")
    print("[+] Bảng boolean df.isnull():")
    print(df_prop.isnull())
    print("\n[+] Số lượng giá trị thiếu theo từng cột (df.isnull().sum()):")
    print(df_prop.isnull().sum())

    # 2.3. Xem cột NUM_BEDROOMS và tìm những giá trị NaN
    print("\n--- 2.3 Xem cột NUM_BEDROOMS và tìm những giá trị NaN ---")
    print("[+] Giá trị của cột NUM_BEDROOMS:")
    print(df_prop['NUM_BEDROOMS'])
    print("\n[+] Kiểm tra isnull trên cột NUM_BEDROOMS:")
    print(df_prop['NUM_BEDROOMS'].isnull())
    print("\n[+] Các dòng có NUM_BEDROOMS là NaN:")
    print(df_prop[df_prop['NUM_BEDROOMS'].isnull()])

    # 2.4. Tổng giá trị còn thiếu trong Dataframe
    print("\n--- 2.4 Tổng giá trị còn thiếu trong Dataframe ---")
    total_missing = df_prop.isnull().sum().sum()
    print(f"[+] Tổng số lượng giá trị còn thiếu trong toàn bộ Dataframe: {total_missing}")

    # 2.5a. Điền giá trị 126 vào ô bị thiếu trong cột “ST_NUM”
    print("\n--- 2.5a Điền giá trị 126 vào ô bị thiếu trong cột ST_NUM ---")
    print("Trước khi điền:")
    print(df_prop[['PID', 'ST_NUM', 'ST_NAME']])
    df_prop['ST_NUM'] = df_prop['ST_NUM'].fillna(126)
    print("\nSau khi điền 126 vào ST_NUM:")
    print(df_prop[['PID', 'ST_NUM', 'ST_NAME']])

    # 2.5b. Thay thế missing values trong cột “NUM_BEDROOMS” bằng giá trị trung vị (median)
    print("\n--- 2.5b Thay thế missing values trong NUM_BEDROOMS bằng median ---")
    median_val = df_prop['NUM_BEDROOMS'].median()
    print(f"[+] Giá trị trung vị (median) của NUM_BEDROOMS: {median_val}")
    print("\nTrước khi điền median vào NUM_BEDROOMS:")
    print(df_prop[['PID', 'NUM_BEDROOMS']])
    df_prop['NUM_BEDROOMS'] = df_prop['NUM_BEDROOMS'].fillna(median_val)
    print("\nSau khi điền median vào NUM_BEDROOMS:")
    print(df_prop[['PID', 'NUM_BEDROOMS']])

    print("\n[+] Toàn bộ DataFrame sau khi đã hoàn thành các bước làm sạch:")
    print(df_prop)

if __name__ == '__main__':
    main()
