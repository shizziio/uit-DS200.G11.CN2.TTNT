"""Lab 4 (P1): khám phá Moneyball và xử lý dữ liệu thiếu của Netflix 2019."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import scatter_matrix
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Lasso, LinearRegression, Ridge
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "datasets" / "lab4"
OUTPUT_DIR = Path(__file__).resolve().parent / "outputs"


def moneyball():
    print("\n=== I. MONEYBALL (OpenML 41021) ===")
    data = pd.read_csv(DATA_DIR / "moneyball.csv")
    X = data.drop(columns="RS")
    y = data["RS"]
    print(f"Kích thước: {data.shape}; mục tiêu: RS (số runs ghi được)")
    print("Giá trị thiếu theo cột:\n" + data.isna().sum().loc[lambda s: s.gt(0)].to_string())

    # Team và League là chuỗi; các cột còn lại được CSV lưu dưới dạng số.
    numeric = X.select_dtypes(include="number")
    print("Các biến số dùng để vẽ/mô hình:", ", ".join(numeric.columns))
    imputer = SimpleImputer(strategy="median")
    clean = pd.DataFrame(imputer.fit_transform(numeric), columns=numeric.columns)
    clean["RS"] = y.to_numpy()
    assert not clean.isna().any().any()

    axes = scatter_matrix(clean, c=clean["RS"], figsize=(18, 18),
                          marker="o", s=8, alpha=0.5, cmap="viridis",
                          diagonal="hist", hist_kwds={"bins": 20})
    fig = axes[0, 0].figure
    fig.suptitle("Moneyball: ma trận phân tán, màu theo RS", y=1.0)
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "moneyball_scatter_matrix.png", dpi=110)
    plt.close(fig)

    # Fit imputer/scaler trong pipeline chỉ trên train để tránh rò rỉ dữ liệu.
    X_train, X_test, y_train, y_test = train_test_split(
        numeric, y, test_size=0.2, random_state=42
    )
    print("\nSo sánh hồi quy trên tập test (80/20, random_state=42):")
    for name, estimator in [
        ("LinearRegression", LinearRegression()),
        ("Ridge", Ridge(alpha=1.0)),
        ("Lasso", Lasso(alpha=1.0, max_iter=10000)),
    ]:
        model = make_pipeline(SimpleImputer(strategy="median"), StandardScaler(), estimator)
        model.fit(X_train, y_train)
        prediction = model.predict(X_test)
        print(f"{name:17s} R²={r2_score(y_test, prediction):.4f}  MAE={mean_absolute_error(y_test, prediction):.2f}")

    correlations = clean.corr(numeric_only=True)["RS"].drop("RS")
    correlations = correlations.reindex(correlations.abs().sort_values(ascending=False).index)
    print("\nTương quan Pearson với RS:\n" + correlations.to_string())


def netflix():
    print("\n=== II. NETFLIX 2019 ===")
    data = pd.read_csv(DATA_DIR / "netflix_titles_2019.csv")
    print(f"Kích thước: {data.shape}")
    print("Kiểu dữ liệu:\n" + data.dtypes.to_string())
    print("Số ô thiếu theo cột:\n" + data.isna().sum().sort_values(ascending=False).to_string())
    print("Tỷ lệ thiếu theo cột (%):\n" + (data.isna().mean() * 100).round(2).to_string())
    print("Ví dụ các dòng thiếu director:\n" + data.loc[data["director"].isna(), ["show_id", "title", "director"]].head().to_string(index=False))

    # Minh họa các lựa chọn trong đề trên bản sao, không sửa dữ liệu gốc.
    print(f"Nếu bỏ cột director: {data.drop(columns='director').shape[1]} cột")
    print(f"Nếu bỏ dòng thiếu director: {len(data.dropna(subset=['director']))} dòng")

    clean = data.copy()
    for column in ["director", "cast", "country", "date_added"]:
        clean[column] = clean[column].fillna("Unknown")
    rating_mode = clean["rating"].mode().iat[0]
    clean["rating"] = clean["rating"].fillna(rating_mode)
    # duration không có ô thiếu trong bộ dữ liệu này; lệnh sau minh họa fillna trong đề.
    clean["duration"] = clean["duration"].fillna("Unknown")
    assert not clean.isna().any().any()
    print(f"Đã điền rating thiếu bằng mode: {rating_mode}")
    print("Số ô thiếu sau xử lý:", int(clean.isna().sum().sum()))

    counts = clean["rating"].value_counts()
    fig, ax = plt.subplots(figsize=(12, 6))
    counts.plot.bar(ax=ax)
    ax.set(title="Phân bố rating Netflix 2019", xlabel="Rating", ylabel="Số chương trình")
    ax.tick_params(axis="x", rotation=45)
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "netflix_rating.png", dpi=150)
    plt.close(fig)
    clean.to_csv(OUTPUT_DIR / "netflix_cleaned.csv", index=False)
    print("Phân bố rating:\n" + counts.to_string())


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)
    moneyball()
    netflix()
    print(f"\nĐã lưu biểu đồ và CSV đã xử lý tại: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
