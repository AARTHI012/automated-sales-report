import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

def create_charts(df, output_dir="reports/charts"):
    Path(output_dir).mkdir(exist_ok=True)
    
    # Revenue by Category
    plt.figure(figsize=(10,6))
    df.groupby('Category')['Total_Amount'].sum().plot(kind='bar')
    plt.title('Revenue by Category')
    plt.savefig(f"{output_dir}/revenue_by_category.png")
    plt.close()
    
    # Trend over time
    plt.figure(figsize=(12,6))
    monthly = df.groupby('Date')['Total_Amount'].sum().resample('D').sum()
    monthly.plot()
    plt.title('Daily Revenue Trend')
    plt.savefig(f"{output_dir}/revenue_trend.png")
    plt.close()
