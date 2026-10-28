# UIT DS200.G11.CN2.TTNT – Bài tập Dữ liệu lớn

## Cấu trúc

- `de-bai/`: PDF đề bài của từng lab.
- `datasets/lab1/`: CSV kết quả thu thập từ VnExpress.
- `datasets/lab2/`: `employees.csv`.
- `datasets/lab3/`: `sample_data.csv` và `property_data.csv`.
- `lab1/`, `lab2/`, `lab3/`: notebook, script và hướng dẫn từng bài.

## Chạy trên Google Colab

Mở notebook tương ứng từ GitHub. Lab 2 và Lab 3 đọc dữ liệu trực tiếp qua GitHub Raw, nên không cần tải CSV thủ công hoặc mount Google Drive. Ví dụ:

```python
import pandas as pd
url = "https://raw.githubusercontent.com/shizziio/uit-DS200.G11.CN2.TTNT/main/datasets/lab2/employees.csv"
data = pd.read_csv(url)
```

Lab 1 thu thập dữ liệu mới từ web; các CSV có sẵn trong `datasets/lab1/` là kết quả tham khảo. Khi chạy notebook, kết quả mới được ghi vào `datasets/lab1/` trong môi trường hiện tại.

Các script `lab2.py` và `lab3.py` cũng đọc dữ liệu từ GitHub Raw, nên cần kết nối Internet.
