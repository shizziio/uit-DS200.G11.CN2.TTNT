"""
Lab 1: Thu Thập Dữ Liệu Web (Web Scraping)
Thực hành crawl dữ liệu tin tức từ VnExpress và lưu vào file CSV.
"""

import csv
import time
import requests
from bs4 import BeautifulSoup

def crawl_vnexpress_category(category_url: str, max_articles: int = 15):
    """
    Thu thập danh sách bài viết từ một danh mục VnExpress và lấy chi tiết từng bài.
    """
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
    }

    print(f"[*] Đang gửi request tới danh mục: {category_url}")
    response = requests.get(category_url, headers=headers, timeout=10)
    if response.status_code != 200:
        print(f"[!] Không thể truy cập trang. Mã lỗi HTTP: {response.status_code}")
        return []

    soup = BeautifulSoup(response.content, "html.parser")
    # Trên VnExpress, tiêu đề tin tức có thể nằm trong h2 hoặc h3 có class title-news
    titles = soup.find_all(["h2", "h3"], class_="title-news")
    print(f"[*] Tìm thấy {len(titles)} bài viết trong danh mục.")

    links = []
    for item in titles:
        a_tag = item.find("a")
        if a_tag and a_tag.get("href"):
            link = a_tag["href"]
            # Chỉ lấy các bài viết html thông thường
            if link.startswith("https://vnexpress.net/") and link.endswith(".html"):
                if link not in links:
                    links.append(link)
        if len(links) >= max_articles:
            break

    print(f"[*] Sẽ tiến hành crawl chi tiết {len(links)} bài viết...\n")

    articles_data = []

    for idx, link in enumerate(links, 1):
        try:
            print(f"[{idx}/{len(links)}] Đang cào: {link}")
            news_res = requests.get(link, headers=headers, timeout=10)
            if news_res.status_code != 200:
                print(f"    -> Lỗi tải bài ({news_res.status_code}), bỏ qua.")
                continue

            news_soup = BeautifulSoup(news_res.content, "html.parser")

            # Tìm tiêu đề (thử thẻ có class 'title-detail' trước theo lab, nếu không có lấy thẻ h1 bất kỳ)
            title_node = news_soup.find("h1", class_="title-detail") or news_soup.find("h1")
            title = title_node.get_text(strip=True) if title_node else "N/A"

            # Tìm mô tả / tóm tắt (thử class 'description' trước theo lab, fallback sang đoạn p đầu tiên)
            desc_node = news_soup.find("p", class_="description") or news_soup.find("p")
            description = desc_node.get_text(strip=True) if desc_node else "N/A"

            print(f"    - Tiêu đề : {title}")
            print(f"    - Mô tả   : {description[:90]}...\n")

            articles_data.append({
                "STT": idx,
                "Tiêu đề": title,
                "Mô tả": description,
                "Đường dẫn": link
            })

            # Nghỉ ngắn giữa các request để lịch sự và tránh bị rate limit
            time.sleep(0.5)

        except Exception as e:
            print(f"    -> Lỗi khi xử lý bài viết: {e}")

    return articles_data


def save_to_csv(data: list, output_filename: str):
    """
    Lưu danh sách bài viết vào file CSV định dạng UTF-8 có BOM để mở bằng Excel không lỗi font.
    """
    if not data:
        print("[!] Không có dữ liệu để lưu vào file CSV.")
        return

    fields = ["STT", "Tiêu đề", "Mô tả", "Đường dẫn"]
    from pathlib import Path
    output_path = Path(__file__).resolve().parent.parent / "datasets" / "lab1" / output_filename
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open(mode="w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)

    print(f"[✓] Đã xuất thành công {len(data)} bài viết vào file: {output_path}")


if __name__ == "__main__":
    # 1. Thực hành với trang bóng đá theo tài liệu Lab 1
    bongda_url = "https://vnexpress.net/bong-da"
    print("=" * 60)
    print("PHẦN 1: CRAWL CHUYÊN MỤC BÓNG ĐÁ THEO YÊU CẦU LAB 1")
    print("=" * 60)
    bongda_articles = crawl_vnexpress_category(bongda_url, max_articles=10)
    save_to_csv(bongda_articles, "vnexpress_bongda.csv")

    # 2. Thực hành mở rộng với trang công nghệ theo yêu cầu mục 6
    khoahoc_url = "https://vnexpress.net/khoa-hoc"
    print("\n" + "=" * 60)
    print("PHẦN 2: THỰC HÀNH MỞ RỘNG (MỤC 6) - CRAWL CHUYÊN MỤC KHOA HỌC")
    print("=" * 60)
    khoahoc_articles = crawl_vnexpress_category(khoahoc_url, max_articles=10)
    save_to_csv(khoahoc_articles, "vnexpress_khoahoc.csv")
