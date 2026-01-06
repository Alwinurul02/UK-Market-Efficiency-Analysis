import os
import data_cleaning as dc
import analysis_logic as al
import visualization_ibcs as viz

# --- KONFIGURASI PATH (Sesuai punya kamu) ---
BASE_PATH = r"D:/uk-market-analysis"
DATA_DIR = os.path.join(BASE_PATH, "data")
OUTPUT_DIR = os.path.join(BASE_PATH, "output")

TOWNS_FILE = os.path.join(DATA_DIR, "uk-towns.csv")
CUST_FILE = os.path.join(DATA_DIR, "customers.csv")

def main():
    print("=== MULAI PIPELINE ANALISIS DATA ===")
    print(f"Path Data: {DATA_DIR}")

    # 1. CLEANING & PREPARATION
    # Load referensi & logic penyetaraan
    place_map, place_to_county, search_terms = dc.load_and_clean_reference(TOWNS_FILE)
    
    # Bersihkan data pelanggan (Handle Null & Matching)
    df_clean = dc.clean_customer_data(CUST_FILE, search_terms, place_map, place_to_county)

    # 2. BUSINESS ANALYSIS
    # Hitung Revenue per Kota
    df_revenue = al.get_revenue_by_city(df_clean)
    
    # Hitung Efisiensi (Per Capita)
    df_efficiency = al.calculate_efficiency(df_clean)
    
    # Cek Unknown Stats
    unknown_pct = al.get_unknown_stats(df_clean)
    print(f"   [Insight] Persentase Data Unknown: {unknown_pct:.1f}%")

    # 3. VISUALIZATION
    # Grafik 1: Hidden Market (Highlight Kota Baru)
    viz.plot_ibcs_bar(
        data=df_revenue, 
        x_col='total_spend', 
        y_col='City',
        title='Top Revenue Sources (Highlight: The Hidden Market)',
        filename='ibcs_top15_towns.png',
        output_dir=OUTPUT_DIR,
        highlight_items=['Northampton', 'Reading', 'Luton', 'Milton Keynes']
    )

    # Grafik 2: Efficiency (Highlight Manchester)
    viz.plot_ibcs_bar(
        data=df_efficiency,
        x_col='Spend_Per_Capita',
        y_col='City',
        title='Market Efficiency: Spend Per Capita (Winner: Manchester)',
        filename='ibcs_efficiency.png',
        output_dir=OUTPUT_DIR,
        fmt='£{:.2f}',
        highlight_items=['Manchester', 'Reading']
    )

    print(f"\n=== SELESAI! Cek hasil di: {OUTPUT_DIR} ===")

if __name__ == "__main__":
    main()
