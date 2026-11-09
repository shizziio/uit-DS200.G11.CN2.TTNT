"""Lab 5 (P2): trích văn bản PDF và tiền xử lý tiếng Anh với NLTK."""

import re
from pathlib import Path

import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer, WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize
from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
BOOK_PATH = ROOT / "datasets" / "lab5" / "book.pdf"
OTHER_PATH = ROOT / "datasets" / "lab5" / "thinkstats2.pdf"
REQUIRED_NLTK_DATA = {
    "punkt_tab": "tokenizers/punkt_tab/english/",
    "stopwords": "corpora/stopwords",
    "wordnet": "corpora/wordnet.zip",
}


def ensure_nltk_data():
    """Chỉ tải các tài nguyên cần dùng, không tải toàn bộ kho NLTK."""
    for package, resource in REQUIRED_NLTK_DATA.items():
        try:
            nltk.data.find(resource)
        except LookupError:
            if not nltk.download(package, quiet=True):
                raise RuntimeError(f"Không tải được tài nguyên NLTK: {package}")


def read_page(path: Path, page_index: int) -> str:
    reader = PdfReader(path)
    if page_index >= len(reader.pages):
        raise ValueError(f"{path.name} chỉ có {len(reader.pages)} trang")
    text = reader.pages[page_index].extract_text() or ""
    if not text.strip():
        raise ValueError(f"Không trích được văn bản từ trang {page_index + 1} của {path.name}")
    return text


def normalize_text(text: str) -> str:
    # PDF ngắt một từ ở cuối dòng như "main-\nstays".
    text = re.sub(r"(?<=\w)-\s*\n(?=\w)", "", text)
    return re.sub(r"\s+", " ", text).strip().casefold()


def tokenize_and_transform(text: str) -> dict:
    sentences = sent_tokenize(text)
    raw_tokens = word_tokenize(text)
    words = [token for token in raw_tokens if token.isalpha()]
    english_stopwords = set(stopwords.words("english"))
    filtered = [token for token in words if token not in english_stopwords]
    stemmer = SnowballStemmer("english")
    lemmatizer = WordNetLemmatizer()
    return {
        "sentences": sentences,
        "tokens": raw_tokens,
        "words": words,
        "without_stopwords": filtered,
        "stems": [stemmer.stem(token) for token in filtered],
        "lemmas": [lemmatizer.lemmatize(token, pos="v") for token in filtered],
    }


def print_summary(name: str, result: dict):
    print(f"\n{name}")
    for key in ("sentences", "tokens", "words", "without_stopwords"):
        examples = result[key][:2] if key == "sentences" else result[key][:12]
        print(f"{key}: {len(result[key])}; ví dụ: {examples}")
    print("Stemming (12 từ đầu):", result["stems"][:12])
    print("Lemmatization, pos='v' (12 từ đầu):", result["lemmas"][:12])


def main():
    ensure_nltk_data()

    print("=== I. THỰC HÀNH: BOOK.PDF ===")
    book_page = read_page(BOOK_PATH, 10)  # Trang thứ 11, tương ứng ảnh trong đề.
    lower = book_page.casefold()
    over_index = lower.find("over")
    if over_index < 0:
        raise ValueError("Không tìm thấy 'over' trong trang sách")
    print(f"Số ký tự trích được: {len(book_page)}; vị trí 'over' đầu tiên: {over_index}")
    excerpt = lower[over_index:]
    # Bỏ tiêu đề giữa văn bản, rồi tìm và cắt đoạn sau dấu mốc của đề.
    excerpt = re.sub(r"1\.1 a taste of machine learning|1\.1\.1 applications", " ", excerpt)
    goal_index = excerpt.find("to achieve this goal")
    if goal_index < 0:
        raise ValueError("Không tìm thấy 'to achieve this goal' trong đoạn sách")
    excerpt = normalize_text(excerpt[:goal_index])
    print(f"Vị trí mốc cuối: {goal_index}; độ dài đoạn sau xử lý: {len(excerpt)}")
    print_summary("Kết quả book.pdf:", tokenize_and_transform(excerpt))

    print("\n=== II. BÀI TẬP: PDF KHÁC ===")
    other_page = read_page(OTHER_PATH, 20)  # Trang PDF thứ 21, mở đầu Chương 1.
    start = other_page.find("The thesis of this book is")
    end = other_page.find("Reports like these are called", start)
    if start < 0 or end < 0:
        raise ValueError("Không tìm thấy đoạn cần xử lý trong thinkstats2.pdf")
    other_excerpt = normalize_text(other_page[start:end])
    print(f"Tệp: {OTHER_PATH.name}; trang 21; độ dài đoạn: {len(other_excerpt)}")
    print_summary("Kết quả thinkstats2.pdf:", tokenize_and_transform(other_excerpt))

    print("\nVí dụ phân biệt stemming và lemmatization:")
    stemmer = SnowballStemmer("english")
    lemmatizer = WordNetLemmatizer()
    for word in ("walking", "went", "mice"):
        print(f"{word}: stem={stemmer.stem(word)}, lemma(verb)={lemmatizer.lemmatize(word, pos='v')}, lemma(noun)={lemmatizer.lemmatize(word, pos='n')}")


if __name__ == "__main__":
    main()
