# LAB 1: THU THẬP DỮ LIỆU WEB (WEB SCRAPING)
**Mã số SV**: 26410022  
**Học phần**: Dữ liệu lớn (Big Data)

---

## 1. Cấu trúc thư mục `lab1`

- `crawler.py`: Script Python thực hiện đầy đủ quy trình crawl từ VnExpress (Bóng đá & Khoa học), sau đó xuất ra các file CSV.
- `lab1.ipynb`: Jupyter Notebook từng bước (step-by-step) theo đúng trình tự hướng dẫn trong `../de-bai/lab1.pdf` (gửi request, parse DOM bằng BeautifulSoup, trích xuất thuộc tính, lưu CSV và phân tích bằng Pandas).
- `../datasets/lab1/vnexpress_bongda.csv`: Dữ liệu bài viết bóng đá crawl được (Tiêu đề, Mô tả, Link).
- `../datasets/lab1/vnexpress_khoahoc.csv`: Dữ liệu bài viết khoa học (phần mở rộng mục 6 của Lab).

---

## 2. Cách chạy

### Chạy bằng script Python:
```bash
python3 lab1/crawler.py
```

### Chạy bằng Jupyter Notebook:
Mở file `lab1/lab1.ipynb` bằng VS Code / Jupyter Lab và thực thi tuần tự các cell.

Các CSV tạo mới được lưu trong `datasets/lab1/`.
