# UIT DS200.G11.CN2.TTNT – Bài tập Dữ liệu lớn

**GitHub repository:** [shizziio/uit-DS200.G11.CN2.TTNT](https://github.com/shizziio/uit-DS200.G11.CN2.TTNT)

| Bài lab | Notebook | Đề bài |
| --- | --- | --- |
| Lab 1 | [Mở trên Google Colab](https://colab.research.google.com/github/shizziio/uit-DS200.G11.CN2.TTNT/blob/main/lab1/lab1.ipynb) | [lab1.pdf](de-bai/lab1.pdf) |
| Lab 2 | [Mở trên Google Colab](https://colab.research.google.com/github/shizziio/uit-DS200.G11.CN2.TTNT/blob/main/lab2/lab2.ipynb) | [Lab 2_1 Missing Data.pdf](de-bai/Lab%202_1%20Missing%20Data.pdf) |
| Lab 3 | [Mở trên Google Colab](https://colab.research.google.com/github/shizziio/uit-DS200.G11.CN2.TTNT/blob/main/lab3/lab3.ipynb) | [Lab 3_Clearning Data.pdf](de-bai/Lab%203_Clearning%20Data.pdf) |
| Lab 3.1 | [Mở trên Google Colab](https://colab.research.google.com/github/shizziio/uit-DS200.G11.CN2.TTNT/blob/main/lab3_1/lab3_1.ipynb) | [LAB-3.1.pdf](de-bai/LAB-3.1.pdf) |
| Lab 4 (P1) | [Mở trên Google Colab](https://colab.research.google.com/github/shizziio/uit-DS200.G11.CN2.TTNT/blob/main/lab4/lab4.ipynb) | [Lab 4_Data preprocessing_p1.pdf](de-bai/Lab%204_Data%20preprocessing_p1.pdf) |
| Lab 5 (P2) | [Mở trên Google Colab](https://colab.research.google.com/github/shizziio/uit-DS200.G11.CN2.TTNT/blob/main/lab5/lab5.ipynb) | [Lab 5_Data preprocessing_p2.docx](de-bai/Lab%205_Data%20preprocessing_p2.docx) |

## Cấu trúc

- `de-bai/`: PDF/DOCX đề bài của từng lab.
- `datasets/lab1/`: CSV kết quả thu thập từ VnExpress.
- `datasets/lab2/`: `employees.csv`.
- `datasets/lab3/`: `sample_data.csv` và `property_data.csv`.
- `datasets/lab3_1/`: `Salary_Data.csv` cho bài hồi quy tuyến tính.
- `datasets/lab4/`: Moneyball và Netflix 2019 cho bài tiền xử lý dữ liệu.
- `datasets/lab5/`: `book.pdf` của đề và `thinkstats2.pdf` cho bài tiền xử lý văn bản.
- `lab1/`, `lab2/`, `lab3/`, `lab3_1/`, `lab4/`, `lab5/`: notebook, script và hướng dẫn từng bài.

## Chạy trên Google Colab

Mở notebook tương ứng từ GitHub. Lab 2, Lab 3, Lab 3.1, Lab 5 và phần Netflix của Lab 4 đọc dữ liệu qua GitHub Raw trên Colab; phần Moneyball của Lab 4 tải từ OpenML. Không cần tải dữ liệu thủ công hoặc mount Google Drive. Ví dụ:

```python
import pandas as pd
url = "https://raw.githubusercontent.com/shizziio/uit-DS200.G11.CN2.TTNT/main/datasets/lab2/employees.csv"
data = pd.read_csv(url)
```

Lab 1 thu thập dữ liệu mới từ web; các CSV có sẵn trong `datasets/lab1/` là kết quả tham khảo. Khi chạy notebook, kết quả mới được ghi vào `datasets/lab1/` trong môi trường hiện tại.

Các script `lab2.py` và `lab3.py` cũng đọc dữ liệu từ GitHub Raw, nên cần kết nối Internet.
