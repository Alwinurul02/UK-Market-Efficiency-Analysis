import pandas as pd
import os

def load_and_clean_reference(towns_path):
    """
    1. Memuat referensi kota (uk-towns.csv)
    2. Melakukan penyetaraan data (Aliasing & Filter Bad Words)
    """
    print("   [Cleaning] Memuat referensi kota...")
    if not os.path.exists(towns_path):
        raise FileNotFoundError(f"File tidak ditemukan: {towns_path}")

    df_towns = pd.read_csv(towns_path)
    
    # Ambil hanya City & Town
    town_ref = df_towns[df_towns['type'].isin(['City', 'Town'])][['place_name', 'county']].drop_duplicates('place_name')
    
    # Buat Dictionary Mapping
    place_to_county = dict(zip(town_ref['place_name'], town_ref['county']))
    place_map = {name: name for name in town_ref['place_name']}
    
    # --- PENYETARAAN DATA (ALIASING) ---
    aliases = {
        'Hull': 'Kingston-upon-Hull', 
        'Newcastle': 'Newcastle-upon-Tyne', 
        'Londonderry': 'Derry', 
        'Westminster': 'London',
        'Stoke': 'Stoke on Trent'
    }
    place_map.update(aliases)
    
    # --- MEMBERSIHKAN KATA AMBIGU ---
    bad_words = ['Street', 'Ware', 'March', 'Deal', 'Sandwich', 'Eye', 'Bury', 'Fleet']
    for word in bad_words:
        if word in place_map: del place_map[word]
        
    # Urutkan dari yang terpanjang (Longest Match First)
    search_terms = sorted(place_map.keys(), key=len, reverse=True)
    
    return place_map, place_to_county, search_terms

def clean_customer_data(cust_path, search_terms, place_map, place_to_county):
    """
    1. Handle Null pada alamat
    2. Matching alamat dengan database kota
    """
    print("   [Cleaning] Memproses data pelanggan & Handle Null...")
    if not os.path.exists(cust_path):
        raise FileNotFoundError(f"File tidak ditemukan: {cust_path}")

    df = pd.read_csv(cust_path)

    # Fungsi Matching
    def find_city(address):
        # --- HANDLE NULL / TIPE DATA ---
        if not isinstance(address, str): 
            return "Unknown", "Unknown"
        
        addr_upper = address.upper()
        
        for term in search_terms:
            if term.upper() in addr_upper:
                canonical = place_map[term]
                # Spesial Case London
                if canonical == 'London': 
                    return 'London', 'Greater London'
                
                county = place_to_county.get(canonical, "Unknown")
                return canonical, county
                
        return "Unknown", "Unknown"

    # Terapkan ke DataFrame
    matches = df['address'].apply(lambda x: pd.Series(find_city(x)))
    df['City'] = matches[0]
    df['County'] = matches[1]
    
    return df
