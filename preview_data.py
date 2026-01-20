"""
Script to preview and verify generated data
"""

import pandas as pd
import os
from pathlib import Path

def preview_file(filepath, rows=5):
    """Preview first N rows of an Excel file"""
    try:
        df = pd.read_excel(filepath)
        print(f"\n{'='*80}")
        print(f"File: {os.path.basename(filepath)}")
        print(f"Total Rows: {len(df)}")
        print(f"{'='*80}")
        print(df.head(rows).to_string())
        print(f"\n... ({len(df) - rows} more rows) ...\n")
    except Exception as e:
        print(f"Error reading {filepath}: {e}")

def main():
    data_dir = Path("generated_data")
    
    if not data_dir.exists():
        print("No generated data found! Run data_generator.py first.")
        return
    
    files = sorted(data_dir.glob("*.xlsx"))
    
    if not files:
        print("No Excel files found in generated_data/")
        return
    
    print("\n" + "="*80)
    print("DATA GENERATOR - PREVIEW & VERIFICATION")
    print("="*80)
    
    for filepath in files:
        preview_file(filepath, rows=3)
    
    print("="*80)
    print(f"Total Files Generated: {len(files)}")
    print("="*80)
    
    # Summary
    print("\nSUMMARY:")
    for filepath in files:
        try:
            df = pd.read_excel(filepath)
            filename = filepath.name
            
            # Get range of values
            weight_cols = [c for c in df.columns if 'Weight' in c]
            strength_7d_cols = [c for c in df.columns if '7d' in c]
            strength_28d_cols = [c for c in df.columns if '28d' in c]
            
            if weight_cols:
                weight_min = df[weight_cols].min().min()
                weight_max = df[weight_cols].max().max()
                print(f"\n{filename}:")
                print(f"  Rows: {len(df)}")
                print(f"  Weight Range: {weight_min:.3f} - {weight_max:.3f}")
                
                if strength_7d_cols:
                    s7d_min = df[strength_7d_cols].min().min()
                    s7d_max = df[strength_7d_cols].max().max()
                    print(f"  7-Day Strength Range: {s7d_min:.2f} - {s7d_max:.2f}")
                
                if strength_28d_cols:
                    s28d_min = df[strength_28d_cols].min().min()
                    s28d_max = df[strength_28d_cols].max().max()
                    print(f"  28-Day Strength Range: {s28d_min:.2f} - {s28d_max:.2f}")
        
        except Exception as e:
            print(f"\nError processing {filepath.name}: {e}")

if __name__ == "__main__":
    main()
