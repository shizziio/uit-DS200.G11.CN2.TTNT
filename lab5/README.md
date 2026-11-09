# Lab 5: Tiền xử lý văn bản từ PDF (P2)

**Học phần:** Dữ liệu lớn (Big Data)

**Mã số sinh viên:** 26410022

**Đề bài:** [Lab 5_Data preprocessing_p2.docx](../de-bai/Lab%205_Data%20preprocessing_p2.docx)

## Dữ liệu và tệp

- `../datasets/lab5/book.pdf`: sách *An Introduction to Machine Learning* được tải từ [liên kết Google Drive trong đề](https://drive.google.com/file/d/1iMJLPfliCWIpxR8mOqMWoM4j8ZMGxIIU/view?usp=sharing). Bài dùng trang PDF thứ 11 (chỉ số `10`), đúng trang được chụp trong đề.
- `../de-bai/LAB-3.1.pdf`: PDF khác dùng cho phần bài tập. Chỉ lấy đoạn tiếng Anh ở trang đầu vì bộ stop words và WordNet được dùng là tiếng Anh.
- `lab5.py`: script thực hiện toàn bộ quy trình và in số lượng cùng ví dụ token ở từng bước.
- `lab5.ipynb`: notebook có giải thích và output; đọc tệp cục bộ khi có, hoặc GitHub Raw trên Colab.

## Nội dung

1. Dùng `pypdf.PdfReader` trích văn bản từ một trang PDF.
2. Chuyển chữ thường, tìm `over`, cắt tiêu đề đầu trang, bỏ tiêu đề con, tìm và cắt trước cụm `to achieve this goal`. Ghép từ bị xuống dòng trong PDF.
3. Tách câu và từ bằng NLTK, bỏ dấu câu và stop words tiếng Anh.
4. Stemming với `SnowballStemmer`; lemmatization với `WordNetLemmatizer(pos='v')`, kèm ví dụ so sánh dạng động từ và danh từ.
5. Lặp lại trên `LAB-3.1.pdf` để giải bài tập cuối đề.

`nltk.download()` chỉ tải `punkt_tab`, `stopwords`, `wordnet` nếu thiếu, không tải toàn bộ dữ liệu NLTK. Thao tác lemmatization dùng `pos='v'` theo ví dụ; khi xử lý văn bản thực tế, nên gán đúng loại từ cho từng token. `pypdf` chỉ trích được chữ có lớp văn bản; tài liệu scan dạng ảnh cần OCR.

## Chạy

Từ thư mục gốc của repo:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install pypdf nltk
python lab5/lab5.py
```

Mở `lab5/lab5.ipynb` trên Jupyter/VS Code hoặc qua liên kết Colab ở README gốc rồi chạy lần lượt từ trên xuống. Notebook tự cài hai thư viện nếu môi trường chưa có.

## Kết quả kiểm tra

Với `pypdf` 7.0.0 và `nltk` 3.10.4, trang sách trích được 2.106 ký tự; `over` đầu tiên ở vị trí 15. Sau khi làm sạch đoạn được chọn: 16 câu, 369 token, 334 token là chữ, còn 178 từ sau khi bỏ stop words. Kết quả có thể chênh nhẹ giữa các phiên bản thư viện do cách trích văn bản và tách câu.
