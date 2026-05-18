import pandas as pd

def generate_summary(df):
    summary = {
        'total_revenue': df['Total_Amount'].sum(),
        'total_units': df['Quantity'].sum(),
        'avg_order_value': df['Total_Amount'].mean(),
        'top_product': df.groupby('Product')['Total_Amount'].sum().idxmax(),
        'top_category': df.groupby('Category')['Total_Amount'].sum().idxmax(),
        'best_region': df.groupby('Region')['Total_Amount'].sum().idxmax()
    }
    return summary

def monthly_summary(df):
    return df.groupby('Month').agg({
        'Total_Amount': 'sum',
        'Quantity': 'sum'
    }).reset_index()
