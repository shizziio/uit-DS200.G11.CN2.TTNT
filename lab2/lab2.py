"""
Lab 2: Làm việc với dữ liệu bị thiếu (Missing Data) trong thư viện Pandas
MSSV: 26410022
Môn học: Dữ liệu lớn (Big Data)
"""

import numpy as np
import pandas as pd

EMPLOYEES_URL = "https://raw.githubusercontent.com/shizziio/uit-DS200.G11.CN2.TTNT/main/datasets/lab2/employees.csv"


def section_1_detect_missing_data():
    print("=" * 60)
    print("1. Thực hiện đoạn code trong Python để phát hiện dữ liệu bị thiếu")
    print("=" * 60)

    # Tạo dictionary of lists
    dict_data = {
        'Điểm dòng 1': [100, 90, np.nan, 95],
        'Điểm dòng 2': [30, 45, 56, np.nan],
        'Điểm dòng 3': [np.nan, 40, 80, 98],
    }

    # Tạo DataFrame từ dictionary
    df = pd.DataFrame(dict_data)
    print("DataFrame ban đầu:")
    print(df)
    print("\nKết quả kiểm tra dữ liệu khuyết với isnull():")
    print(df.isnull())
    print("\nKết quả kiểm tra dữ liệu không khuyết với notnull():")
    print(df.notnull())


def section_2_working_with_dataset():
    print("\n" + "=" * 60)
    print("2. Thực hiện làm việc với tập hợp dataset cho trước (employees.csv)")
    print("=" * 60)

    # Làm việc với file csv
    data = pd.read_csv(EMPLOYEES_URL)

    # Tạo bool series trả về True nếu có giá trị NaN trong cột 'Gender'
    bool_series = pd.isnull(data["Gender"])

    # Lọc và hiển thị dữ liệu dòng Gender = NaN
    missing_gender = data[bool_series]
    print("Dữ liệu các nhân viên có thuộc tính Gender bị thiếu (NaN):")
    print(missing_gender)
    print(f"\nTổng số nhân viên bị thiếu Gender: {len(missing_gender)} / {len(data)}")


def section_3_impute_missing_values():
    print("\n" + "=" * 60)
    print("3. Điền các giá trị còn thiếu bằng fillna(), replace() và interpolate()")
    print("=" * 60)

    dict_data = {
        'Điểm dòng 1': [100, 90, np.nan, 95],
        'Điểm dòng 2': [30, 45, 56, np.nan],
        'Điểm dòng 3': [np.nan, 40, 80, 98],
    }
    df = pd.DataFrame(dict_data)

    print("\n--- 3.1. Điền giá trị hằng số bằng fillna(0) ---")
    print(df.fillna(0))

    print("\n--- 3.2. Điền giá trị với phương pháp 'pad' (forward fill: ffill) ---")
    # method='pad' / 'ffill'
    try:
        print(df.fillna(method='pad'))
    except TypeError:
        # Trong pandas phiên bản mới hơn, method='pad' khuyến khích dùng df.ffill()
        print(df.ffill())

    print("\n--- 3.3. Thay thế giá trị khuyết với replace() trên dataset employees ---")
    data = pd.read_csv(EMPLOYEES_URL)
    data_new = data.replace(to_replace=np.nan, value=-88)
    print("Dữ liệu sau khi thay thế NaN bằng -88:")
    print(data_new)

    print("\n--- 3.4. Điền giá trị còn thiếu bằng phương pháp nội suy tuyến tính interpolate() ---")
    df_interp = pd.DataFrame({
        "A": [12, 4, 5, None, 1],
        "B": [None, 2, 54, 3, None],
        "C": [20, 16, None, 3, 8],
        "D": [14, 3, None, None, 6],
    })
    print("DataFrame mẫu:")
    print(df_interp)
    print("=" * 32)
    data_interpolated = df_interp.interpolate(method='linear', limit_direction='forward')
    print("DataFrame sau khi interpolate(method='linear', limit_direction='forward'):")
    print(data_interpolated)


if __name__ == "__main__":
    section_1_detect_missing_data()
    section_2_working_with_dataset()
    section_3_impute_missing_values()
