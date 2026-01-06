import matplotlib.pyplot as plt
import os

def plot_ibcs_bar(data, x_col, y_col, title, filename, output_dir, highlight_items=None, fmt='£{:,.0f}'):
    """
    Fungsi visualisasi generic untuk IBCS Style.
    - highlight_items: List nama kota yang ingin diwarnai MERAH.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    full_path = os.path.join(output_dir, filename)
    print(f"   [Viz] Rendering grafik: {filename}...")
    
    # Urutkan data (kecil di atas agar besar di bawah/puncak)
    data_sorted = data.sort_values(by=x_col, ascending=True).tail(15) # Ambil top 15 saja biar rapi
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Logika Warna (Merah jika di highlight, sisanya Abu Gelap)
    colors = []
    for item in data_sorted[y_col]:
        if highlight_items and item in highlight_items:
            colors.append('#C00000') # Merah
        else:
            colors.append('#404040') # Abu-abu
            
    bars = ax.barh(data_sorted[y_col], data_sorted[x_col], color=colors, height=0.6)
    
    # Style Bersih
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(left=False, bottom=False)
    
    # Label Angka
    max_val = data[x_col].max()
    for bar in bars:
        width = bar.get_width()
        label = fmt.format(width)
        ax.text(width + (max_val * 0.01), bar.get_y() + bar.get_height()/2, 
                label, ha='left', va='center', fontsize=10, fontweight='bold')
        
    plt.title(title, loc='left', fontsize=12, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig(full_path)
    plt.close()
