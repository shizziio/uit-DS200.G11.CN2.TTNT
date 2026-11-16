"""Lab 5.2: khám phá và tiền xử lý dữ liệu shopping_trends.csv."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "datasets" / "lab5" / "shopping_trends.csv"
OUTPUT_DIR = Path(__file__).resolve().parent / "outputs"


def audit_data(data: pd.DataFrame) -> None:
    print("Kích thước dữ liệu:", data.shape)
    print("5 dòng đầu:\n", data.head().to_string(index=False))
    print("\nKiểu dữ liệu:\n", data.dtypes.to_string())
    print("\nSố ô thiếu theo cột:\n", data.isna().sum().to_string())
    print("Số dòng trùng hoàn toàn:", int(data.duplicated().sum()))
    print("Số Customer ID trùng:", int(data["Customer ID"].duplicated().sum()))
    print("\nSố giá trị riêng của cột phân loại:\n",
          data.select_dtypes(exclude="number").nunique().to_string())


def prepare_data(data: pd.DataFrame) -> pd.DataFrame:
    """Loại ID/cột lặp thông tin, điền thiếu, mã hóa và chuẩn hóa."""
    if data["Customer ID"].duplicated().any():
        raise ValueError("Customer ID phải là duy nhất")
    redundant = data["Discount Applied"].equals(data["Promo Code Used"])
    print("\nDiscount Applied trùng hoàn toàn Promo Code Used:", redundant)
    drop_columns = ["Customer ID"] + (["Promo Code Used"] if redundant else [])
    features = data.drop(columns=drop_columns)

    numeric_columns = features.select_dtypes(include="number").columns.tolist()
    categorical_columns = features.select_dtypes(exclude="number").columns.tolist()
    transformer = ColumnTransformer(
        transformers=[
            ("num", Pipeline([
                ("impute", SimpleImputer(strategy="median")),
                ("scale", StandardScaler()),
            ]), numeric_columns),
            ("cat", Pipeline([
                ("impute", SimpleImputer(strategy="most_frequent")),
                ("onehot", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
            ]), categorical_columns),
        ],
        verbose_feature_names_out=False,
    )
    matrix = transformer.fit_transform(features)
    processed = pd.DataFrame(matrix, columns=transformer.get_feature_names_out(), index=data.index)
    if processed.isna().any().any():
        raise ValueError("Dữ liệu sau tiền xử lý vẫn còn giá trị thiếu")
    print("Cột số đã chuẩn hóa:", numeric_columns)
    print("Cột phân loại đã one-hot:", categorical_columns)
    print("Kích thước ma trận sau tiền xử lý:", processed.shape)
    return processed


def save_charts(data: pd.DataFrame) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    data["Category"].value_counts().plot.bar(ax=axes[0], color="#377eb8")
    axes[0].set(title="Số giao dịch theo danh mục", xlabel="Danh mục", ylabel="Số giao dịch")
    data["Purchase Amount (USD)"].plot.hist(ax=axes[1], bins=16, color="#4daf4a", edgecolor="white")
    axes[1].set(title="Phân bố giá trị mua hàng", xlabel="USD", ylabel="Số giao dịch")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "shopping_trends_overview.png", dpi=150)
    plt.close(fig)


def main() -> None:
    data = pd.read_csv(DATA_PATH)
    audit_data(data)
    processed = prepare_data(data)
    OUTPUT_DIR.mkdir(exist_ok=True)
    processed.to_csv(OUTPUT_DIR / "shopping_trends_preprocessed.csv", index=False)
    save_charts(data)
    print(f"Đã lưu CSV và biểu đồ tại: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
