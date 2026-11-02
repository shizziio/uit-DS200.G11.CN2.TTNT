"""Lab 3.1: Hồi quy tuyến tính đơn giản dự đoán lương theo kinh nghiệm."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # Lưu hình khi chạy script, kể cả trên máy không có màn hình.
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "datasets" / "lab3_1" / "Salary_Data.csv"
OUTPUT_DIR = Path(__file__).resolve().parent / "outputs"


def save_scatter(x, y, title, filename, model=None):
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.scatter(x, y, color="red", label="Dữ liệu thực tế")
    if model is not None:
        x_line = pd.DataFrame({"YearsExperience": sorted(x)})
        ax.plot(x_line["YearsExperience"], model.predict(x_line), color="blue", label="Đường hồi quy")
    ax.set(title=title, xlabel="Số năm kinh nghiệm", ylabel="Lương")
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / filename, dpi=150)
    plt.close(fig)


def main():
    dataset = pd.read_csv(DATA_PATH)
    expected_columns = ["YearsExperience", "Salary"]
    if list(dataset.columns) != expected_columns or dataset[expected_columns].isna().any().any():
        raise ValueError(f"Dữ liệu phải có hai cột {expected_columns} và không có giá trị thiếu")

    print("1. Tải dữ liệu")
    print(dataset.head().to_string(index=False))
    print(f"Kích thước: {dataset.shape}")

    X = dataset[["YearsExperience"]]
    y = dataset["Salary"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    print(f"Train: {X_train.shape}, {y_train.shape}; Test: {X_test.shape}, {y_test.shape}")

    OUTPUT_DIR.mkdir(exist_ok=True)
    pair = sns.pairplot(dataset)
    pair.fig.savefig(OUTPUT_DIR / "pairplot.png", dpi=150)
    plt.close(pair.fig)
    save_scatter(X_train["YearsExperience"], y_train, "Dữ liệu train", "train_scatter.png")
    save_scatter(X_test["YearsExperience"], y_test, "Dữ liệu test", "test_scatter.png")

    print("\n2. Huấn luyện mô hình hồi quy tuyến tính")
    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    comparison = pd.DataFrame({
        "YearsExperience": X_test["YearsExperience"].to_numpy(),
        "Original Salary": y_test.to_numpy(),
        "Predict Salary": predictions.round(1),
    })
    print(f"Phương trình: Salary = {model.intercept_:.2f} + {model.coef_[0]:.2f} × YearsExperience")
    print(comparison.to_string(index=False))
    print(f"Training R²: {model.score(X_train, y_train):.6f}")
    print(f"Testing R²:  {model.score(X_test, y_test):.6f}")

    save_scatter(X_train["YearsExperience"], y_train, "Hồi quy trên tập train", "train_regression.png", model)
    save_scatter(X_test["YearsExperience"], y_test, "Hồi quy trên tập test", "test_regression.png", model)
    print(f"Đã lưu 5 biểu đồ tại: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
