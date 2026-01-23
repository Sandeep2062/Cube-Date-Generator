import pandas as pd
import numpy as np
import os
from datetime import datetime

def generate_unique_values(min_val, max_val, count, decimals=2, spacing=None, min_gap=0.0):
    """Generate unique random values within range with optional spacing and minimum gap"""
    values = []
    attempts = 0
    max_attempts = 1000
    
    if spacing is None:
        # Default behavior - fill range normally
        while len(values) < count and attempts < max_attempts:
            val = round(np.random.uniform(min_val, max_val), decimals)
            if val not in values and all(abs(val - v) >= min_gap for v in values):
                values.append(val)
            attempts += 1
        
        if len(values) < count:
            while len(values) < count:
                val = values[-1] + round(np.random.uniform(0.001, 0.009), 3)
                if min_val <= val <= max_val and val not in values and all(abs(val - v) >= min_gap for v in values):
                    values.append(round(val, decimals))
    else:
        # With spacing - spread values more across range
        range_size = max_val - min_val
        segment_size = range_size / count
        
        for i in range(count):
            segment_min = min_val + (i * segment_size)
            segment_max = segment_min + segment_size
            
            attempts = 0
            while attempts < 100:
                val = round(np.random.uniform(segment_min, segment_max), decimals)
                if val not in values and all(abs(val - v) >= min_gap for v in values):
                    values.append(val)
                    break
                attempts += 1
    
    return values[:count]

def generate_concrete_data(mix_type, num_rows=1000):
    """Generate concrete cube weight and strength data"""
    
    # Define ranges for different mix types
    weight_ranges = {
        'M10': (8.100, 8.300),
        'M15': (8.100, 8.300),
        'M20': (8.100, 8.300),
        'M25': (8.180, 8.350),
        'M30': (8.100, 8.350),
        'M35': (8.100, 8.350),
        'M40': (8.100, 8.350),
        'M45': (8.200, 8.400),
    }
    
    strength_7d_ranges = {
        'M10': (214.00, 294.40),
        'M15': (290.10, 317.50),
        'M20': (366.10, 408.10),
        'M25': (442.10, 475.10),
        'M30': (518.10, 560.10),
        'M35': (595.10, 632.80),
        'M40': (669.10, 700.10),
        'M45': (735.10, 785.10),
    }
    
    strength_28d_ranges = {
        'M10': (320.10, 362.50),
        'M15': (433.10, 475.10),
        'M20': (547.10, 589.10),
        'M25': (660.1, 700.10),
        'M30': (770.10, 811.1),
        'M35': (880.90, 920.80),
        'M40': (995.10, 1035.1),
        'M45': (1105.35, 1146.0),
    }
    
    data = []
    
    for row_num in range(1, num_rows + 1):
        # Reverse serial number (1000, 999, 998... instead of 1, 2, 3...)
        sn = num_rows - row_num + 1
        
        # Generate weight values (6 different values)
        weight_min, weight_max = weight_ranges[mix_type]
        weights = generate_unique_values(weight_min, weight_max, 6, decimals=3, min_gap=0.015)
        np.random.shuffle(weights)
        
        # Generate 7-day strength values (3 different values)
        str_7d_min, str_7d_max = strength_7d_ranges[mix_type]
        strength_7d = generate_unique_values(str_7d_min, str_7d_max, 3, decimals=2, min_gap=5.0)
        np.random.shuffle(strength_7d)
        
        # Generate 28-day strength values (3 different values)
        str_28d_min, str_28d_max = strength_28d_ranges[mix_type]
        strength_28d = generate_unique_values(str_28d_min, str_28d_max, 3, decimals=2, min_gap=5.0)
        np.random.shuffle(strength_28d)
        
        # Row: Sn + Weights + Empty Column + Strengths
        row = [sn] + weights + [None] + strength_7d + strength_28d
        data.append(row)
    
    columns = ['Sn', 'Weight_1', 'Weight_2', 'Weight_3', 'Weight_4', 'Weight_5', 'Weight_6',
               '', 'Strength_7d_1', 'Strength_7d_2', 'Strength_7d_3',
               'Strength_28d_1', 'Strength_28d_2', 'Strength_28d_3']
    
    df = pd.DataFrame(data, columns=columns)
    return df

def generate_mortar_data(mortar_type, num_rows=1000):
    """Generate mortar cube weight and strength data"""
    
    weight_range = (0.800, 0.835)
    
    # Strength ranges based on mortar type and days
    if mortar_type == '1:4':
        strength_7d_range = (25.20, 33.9)
        strength_28d_range = (40.60, 50.10)
    else:  # 1:6
        strength_7d_range = (15.20, 25.0)
        strength_28d_range = (25.20, 33.9)
    
    data = []
    
    for row_num in range(1, num_rows + 1):
        # Reverse serial number (1000, 999, 998... instead of 1, 2, 3...)
        sn = num_rows - row_num + 1
        
        # Generate weight values (6 different values)
        weights = generate_unique_values(weight_range[0], weight_range[1], 6, decimals=3)
        np.random.shuffle(weights)
        
        # Generate 7-day strength values (3 different values)
        strength_7d = generate_unique_values(strength_7d_range[0], strength_7d_range[1], 3, decimals=2, min_gap=1.0)
        np.random.shuffle(strength_7d)
        
        # Generate 28-day strength values (3 different values)
        strength_28d = generate_unique_values(strength_28d_range[0], strength_28d_range[1], 3, decimals=2, min_gap=1.0)
        np.random.shuffle(strength_28d)
        
        # Row: Sn + Weights + Empty Column + Strengths
        row = [sn] + weights + [None] + strength_7d + strength_28d
        data.append(row)
    
    columns = ['Sn', 'Weight_1', 'Weight_2', 'Weight_3', 'Weight_4', 'Weight_5', 'Weight_6',
               '', 'Strength_7d_1', 'Strength_7d_2', 'Strength_7d_3',
               'Strength_28d_1', 'Strength_28d_2', 'Strength_28d_3']
    
    df = pd.DataFrame(data, columns=columns)
    return df

def save_excel(df, filename):
    """Save dataframe to Excel file"""
    os.makedirs('generated_data', exist_ok=True)
    filepath = os.path.join('generated_data', filename)
    df.to_excel(filepath, index=False, sheet_name='Data')
    print(f"✓ File saved: {filepath}")

def main():
    print("\n" + "="*60)
    print("DATA GENERATOR FOR WEIGHT AND STRENGTH TESTING")
    print("="*60)
    
    while True:
        print("\nChoose an option:")
        print("\n[1] Generate All Concrete Mixes (M10-M45)")
        print("[2] Generate Single Concrete Mix")
        print("[3] Generate Mortar Data (1:4 and 1:6)")
        print("[4] Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            print("\nGenerating all concrete mixes (1000 rows each)...")
            for mix in ['M10', 'M15', 'M20', 'M25', 'M30', 'M35', 'M40', 'M45']:
                df = generate_concrete_data(mix, num_rows=1000)
                filename = f"{mix}.xlsx"
                save_excel(df, filename)
            print("\n✓ All concrete mixes generated successfully!")
        
        elif choice == '2':
            print("\nAvailable mixes: M10, M15, M20, M25, M30, M35, M40, M45")
            mix = input("Enter mix type (e.g., M10): ").strip().upper()
            
            if mix in ['M10', 'M15', 'M20', 'M25', 'M30', 'M35', 'M40', 'M45']:
                rows = input("Enter number of rows (default 1000): ").strip()
                num_rows = int(rows) if rows.isdigit() else 1000
                
                print(f"\nGenerating {mix} data ({num_rows} rows)...")
                df = generate_concrete_data(mix, num_rows=num_rows)
                filename = f"{mix}.xlsx"
                save_excel(df, filename)
            else:
                print("✗ Invalid mix type!")
        
        elif choice == '3':
            print("\nGenerating mortar data...")
            rows = input("Enter number of rows (default 1000): ").strip()
            num_rows = int(rows) if rows.isdigit() else 1000
            
            print(f"\nGenerating Mortar 1:4 data ({num_rows} rows)...")
            df_14 = generate_mortar_data('1:4', num_rows=num_rows)
            save_excel(df_14, "1_4.xlsx")
            
            print(f"Generating Mortar 1:6 data ({num_rows} rows)...")
            df_16 = generate_mortar_data('1:6', num_rows=num_rows)
            save_excel(df_16, "1_6.xlsx")
            
            print("\n✓ Mortar data generated successfully!")
        
        elif choice == '4':
            print("\nThank you for using Data Generator!")
            break
        
        else:
            print("✗ Invalid choice! Please try again.")
        
        again = input("\nGenerate more data? (y/n): ").strip().lower()
        if again != 'y':
            print("\nThank you for using Data Generator!")
            break

if __name__ == "__main__":
    main()
