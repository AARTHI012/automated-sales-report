from src.data_loader import load_config, load_data
from src.analyzer import generate_summary, monthly_summary
from src.visualizer import create_charts
from src.report_generator import generate_excel_report
from pathlib import Path

def main():
    Path("reports").mkdir(exist_ok=True)
    Path("reports/charts").mkdir(exist_ok=True)
    
    config = load_config()
    df = load_data(config['input']['file'])
    
    summary = generate_summary(df)
    create_charts(df)
    generate_excel_report(df, summary, config)
    
    print("🚀 Automated Reporting Complete!")

if __name__ == "__main__":
    main()
