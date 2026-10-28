
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "WA_Fn-UseC_-Telco-Customer-Churn.csv"
CHARTS_DIR = BASE_DIR / "charts"


def main():
    """Analyze customer churn and retention patterns."""

    if not DATA_PATH.exists():
        print(f"Dataset not found: {DATA_PATH}")
        return

    CHARTS_DIR.mkdir(exist_ok=True)

    df = pd.read_csv(DATA_PATH)

    # Clean column names and prepare data
    df.columns = df.columns.str.strip()
    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"], errors="coerce"
    )
    df = df.drop_duplicates()
    df = df.dropna(subset=["TotalCharges"])

    # Convert churn to a numeric indicator
    df["Churn_Flag"] = df["Churn"].map({"Yes": 1, "No": 0})

    # Calculate key performance indicators
    total_customers = len(df)
    churned_customers = int(df["Churn_Flag"].sum())
    retained_customers = total_customers - churned_customers
    churn_rate = (
        churned_customers / total_customers * 100
        if total_customers else 0
    )
    avg_monthly_charges = df["MonthlyCharges"].mean()
    avg_tenure = df["tenure"].mean()

    print("\n" + "=" * 55)
    print("           CUSTOMER CHURN ANALYSIS")
    print("=" * 55)
    print(f"Total customers:          {total_customers:,}")
    print(f"Customers churned:        {churned_customers:,}")
    print(f"Customers retained:       {retained_customers:,}")
    print(f"Churn rate:               {churn_rate:.2f}%")
    print(f"Average monthly charges:  ${avg_monthly_charges:.2f}")
    print(f"Average customer tenure:  {avg_tenure:.1f} months")

    # Churn by contract type
    contract_summary = (
        df.groupby("Contract")
        .agg(
            Customers=("customerID", "count"),
            Churn_Rate=("Churn_Flag", "mean")
        )
    )
    contract_summary["Churn_Rate"] *= 100

    print("\nChurn by contract type:")
    print(contract_summary.round(2).to_string())

    # Churn by internet service
    internet_summary = (
        df.groupby("InternetService")
        .agg(
            Customers=("customerID", "count"),
            Churn_Rate=("Churn_Flag", "mean")
        )
    )
    internet_summary["Churn_Rate"] *= 100

    print("\nChurn by internet service:")
    print(internet_summary.round(2).to_string())

    # Churn by tenure group
    df["Tenure Group"] = pd.cut(
        df["tenure"],
        bins=[-1, 12, 24, 48, 72],
        labels=["0-12 months", "13-24 months",
                "25-48 months", "49-72 months"]
    )

    tenure_summary = (
        df.groupby("Tenure Group", observed=False)["Churn_Flag"]
        .mean() * 100
    )

    print("\nChurn rate by tenure group (%):")
    print(tenure_summary.round(2).to_string())

    # Chart 1: Overall churn distribution
    churn_counts = df["Churn"].value_counts().reindex(["No", "Yes"])

    plt.figure(figsize=(7, 5))
    churn_counts.plot(kind="bar")
    plt.title("Customer Churn Distribution")
    plt.xlabel("Churn")
    plt.ylabel("Number of Customers")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "churn_distribution.png", dpi=150)
    plt.close()

    # Chart 2: Churn rate by contract
    plt.figure(figsize=(8, 5))
    contract_summary["Churn_Rate"].plot(kind="bar")
    plt.title("Churn Rate by Contract Type")
    plt.xlabel("Contract Type")
    plt.ylabel("Churn Rate (%)")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "churn_by_contract.png", dpi=150)
    plt.close()

    # Chart 3: Churn rate by tenure group
    plt.figure(figsize=(9, 5))
    tenure_summary.plot(kind="bar")
    plt.title("Churn Rate by Customer Tenure")
    plt.xlabel("Tenure Group")
    plt.ylabel("Churn Rate (%)")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "churn_by_tenure.png", dpi=150)
    plt.close()

    # Export summary tables
    contract_summary.to_csv(CHARTS_DIR / "contract_churn_summary.csv")
    internet_summary.to_csv(CHARTS_DIR / "internet_churn_summary.csv")
    tenure_summary.to_csv(CHARTS_DIR / "tenure_churn_summary.csv")

    print(f"\nCharts and reports saved to: {CHARTS_DIR}")
    print("Analysis completed successfully!")


if __name__ == "__main__":
    main()
