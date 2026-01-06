import pandas as pd

def get_revenue_by_city(df):
    """Menghitung Total Revenue per Kota (Top 15)"""
    print("   [Analysis] Menghitung Revenue Aggregation...")
    return df.groupby('City')['total_spend'].sum().reset_index().sort_values(by='total_spend', ascending=False)

def calculate_efficiency(df):
    """
    Analisis Bisnis: Market Efficiency (Spend Per Capita)
    Menggabungkan data revenue dengan estimasi populasi.
    """
    print("   [Analysis] Menghitung Efisiensi Bisnis (Per Capita)...")
    
    # Data Populasi (Hardcoded untuk keperluan analisis)
    pop_estimates = {
        'London': 8900000, 'Birmingham': 1141000, 'Manchester': 550000,
        'Northampton': 225000, 'Reading': 160000, 'Luton': 213000, 'Leeds': 790000
    }
    
    # Filter hanya kota yang ada datanya
    metrics = df[df['City'].isin(pop_estimates.keys())].copy()
    
    # Grouping
    metrics = metrics.groupby('City')['total_spend'].sum().reset_index()
    
    # Kalkulasi Bisnis
    metrics['Population'] = metrics['City'].map(pop_estimates)
    metrics['Spend_Per_Capita'] = metrics['total_spend'] / metrics['Population']
    
    return metrics.sort_values(by='Spend_Per_Capita', ascending=False)

def get_unknown_stats(df):
    """Menghitung % data yang hilang (Unknown)"""
    total = df['total_spend'].sum()
    unknown = df[df['City'] == 'Unknown']['total_spend'].sum()
    return (unknown / total) * 100
