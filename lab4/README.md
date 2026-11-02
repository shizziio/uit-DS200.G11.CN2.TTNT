# Lab 4: Tiền xử lý dữ liệu (P1)

**Học phần:** Dữ liệu lớn (Big Data)
**Mã số sinh viên:** 26410022
**Đề bài:** [Lab 4_Data preprocessing_p1.pdf](../de-bai/Lab%204_Data%20preprocessing_p1.pdf)

## Cấu trúc

- `../datasets/lab4/moneyball.csv`: bản sao [OpenML Moneyball ID 41021](https://www.openml.org/d/41021), gồm 1.232 dòng dữ liệu theo đội bóng/chủ đề mùa giải, mục tiêu `RS` (runs scored).
- `../datasets/lab4/netflix_titles_2019.csv`: CSV 6.234 dòng từ [Google Drive trong đề](https://drive.google.com/file/d/1iH0IU8ybFahoQTTf6A-Ipo6btOj44D1M/view?usp=sharing).
- `lab4.ipynb`: notebook có giải thích, bảng và biểu đồ đã chạy sẵn; dùng CSV cục bộ nếu có. Trên Colab, Moneyball tải qua OpenML và Netflix đọc GitHub Raw.
- `lab4.py`: script chạy hai phần và lưu `moneyball_scatter_matrix.png`, `netflix_rating.png`, `netflix_cleaned.csv` vào `lab4/outputs/`.

## Nội dung

1. **Moneyball:** xem dữ liệu thiếu; bỏ `Team`, `League` khỏi ma trận phân tán; điền trung vị cho các cột số; vẽ ma trận phân tán tô màu theo `RS`; so sánh Linear Regression, Ridge và Lasso trên tập test 20%. Imputer và chuẩn hóa trong pipeline được học riêng trên train để tránh dùng thông tin của test.
2. **Netflix 2019:** xem kiểu dữ liệu, số lượng và tỷ lệ thiếu; minh họa bỏ cột/bỏ dòng trên bản sao; điền `Unknown` cho `director`, `cast`, `country`, `date_added`; điền mode `TV-MA` cho `rating`; vẽ số lượng theo nhãn `rating`. Dữ liệu gốc được giữ nguyên.

Lưu ý: `RankSeason`/`RankPlayoffs` thiếu do nhiều đội không vào playoffs. Trung vị cho hai cột này chỉ phục vụ minh họa thao tác trong đề. Các biến như `W` và `Playoffs` phản ánh kết quả cùng mùa; các điểm hồi quy là bài thực hành, không nên diễn giải như khả năng dự đoán đầu mùa hoặc quan hệ nhân quả.

## Cách chạy

Từ thư mục gốc của repo:

```bash
python3 -m pip install pandas matplotlib scikit-learn
python3 lab4/lab4.py
```

Mở `lab4/lab4.ipynb` trong Jupyter/VS Code hoặc theo liên kết Colab ở README gốc. Sau khi đẩy các tệp mới lên nhánh `main`, Colab đọc được bản Netflix từ GitHub Raw. Không cần cài thêm gói `openml`, vì notebook dùng `sklearn.datasets.fetch_openml`.

## Kết quả kiểm tra

- Moneyball: 1.232 dòng, 15 cột; `RankSeason` và `RankPlayoffs` thiếu 988 ô mỗi cột, `OOBP` và `OSLG` thiếu 812 ô mỗi cột.
- Netflix: 6.234 dòng, 12 cột; `director` thiếu 1.969, `cast` 570, `country` 476, `date_added` 11, `rating` 10. Sau xử lý còn 0 ô thiếu.
- Nhóm `rating` phổ biến nhất sau khi điền mode là `TV-MA`: 2.037 chương trình.
