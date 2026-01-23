# Cube Data Generator for Weight & Strength Testing

Generate synthetic test data for concrete and mortar cube testing with randomized weight and strength values.

## Features

✓ **Multiple Mix Types**: M10, M15, M20, M25, M30, M35, M40, M45  
✓ **Mortar Types**: 1:4 and 1:6 ratios  
✓ **Customizable Rows**: Generate 1000+ rows or any custom amount  
✓ **Unique Values**: Ensures no duplicate values within each row  
✓ **Excel Output**: Direct Excel file generation with proper formatting  
✓ **Easy Menu Interface**: Interactive terminal-based selection  

## Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Setup

```bash
# Install required packages
pip install pandas openpyxl numpy

# For PyInstaller conversion (optional)
pip install pyinstaller
```

### Quick Start

For Windows users:
```cmd
run.bat
```

For Linux/Mac users:
```bash
chmod +x run.sh
./run.sh
```

## Usage

### Running as Python Script

```bash
python data_generator.py
```

### Menu Options

1. **Generate All Concrete Mixes** - Creates M10-M45 with 1000 rows each
2. **Generate Single Concrete Mix** - Choose specific mix (M10-M45) with custom row count
3. **Generate Mortar Data** - Creates 1:4 and 1:6 mortar data
4. **Exit** - Close the program

### Previewing Generated Data

To preview and verify the generated data:

```bash
python preview_data.py
```

This will display a summary of all generated Excel files with sample rows and value ranges.

### Output Files

Generated files are saved in the `generated_data/` folder:

**Concrete Files:**
- `M10.xlsx` (8.100-8.300 weight range)
- `M15.xlsx` (8.100-8.300 weight range)
- `M20.xlsx` (8.100-8.300 weight range)
- `M25.xlsx` (8.100-8.350 weight range)
- `M30.xlsx` (8.100-8.350 weight range)
- `M35.xlsx` (8.100-8.350 weight range)
- `M40.xlsx` (8.100-8.350 weight range)
- `M45.xlsx` (8.100-8.350 weight range)

**Mortar Files:**
- `Mortar_1_4.xlsx` (1:4 mortar ratio)
- `Mortar_1_6.xlsx` (1:6 mortar ratio)

## Data Ranges

### Concrete Mixes (Weight in kg, Strength in kN)

| Mix  | Weight Range | 7-Day Strength | 28-Day Strength |
|------|-------------|----------------|-----------------|
| M10  | 8.10-8.30   | 214.00-294.40  | 320.10-362.50   |
| M15  | 8.10-8.30   | 290.10-317.50  | 433.10-475.10   |
| M20  | 8.10-8.30   | 366.10-408.10  | 547.10-589.10   |
| M25  | 8.10-8.35   | 442.10-475.10  | 660.10-700.10   |
| M30  | 8.10-8.35   | 518.10-560.10  | 770.10-811.10   |
| M35  | 8.10-8.35   | 595.10-632.80  | 880.90-920.80   |
| M40  | 8.200-8.40   | 669.10-700.10  | 995.10-1035.10  |
| M45  | 8.200-8.40   | 735.10-785.10  | 1105.35-1146.00 |

### Mortar Mixes

**1:4 Mortar:**
- Weight: 0.800-0.835 kg
- 7-Day Strength: 25.20-33.90 kN
- 28-Day Strength: 40.60-50.10 kN

**1:6 Mortar:**
- Weight: 0.800-0.835 kg
- 7-Day Strength: 15.20-25.00 kN
- 28-Day Strength: 25.20-33.90 kN

## Excel File Format

Each file contains the following columns:

| Column | Description |
|--------|-------------|
| Sn | Serial Number (1, 2, 3...) |
| Weight_1 to Weight_6 | Six weight measurements (unique values) |
| Strength_7d_1 to Strength_7d_3 | Three 7-day strength measurements |
| Strength_28d_1 to Strength_28d_3 | Three 28-day strength measurements |

### Example Data Row
```
Sn: 1
Weight_1: 8.125, Weight_2: 8.250, Weight_3: 8.198, Weight_4: 8.267, Weight_5: 8.298, Weight_6: 8.304
Strength_7d_1: 293.09, Strength_7d_2: 287.64, Strength_7d_3: 303.00
Strength_28d_1: 464.85, Strength_28d_2: 447.39, Strength_28d_3: 468.82
```

## Customization

You can modify the data ranges in the `data_generator.py` file:

```python
weight_ranges = {
    'M10': (8.100, 8.300),
    'M15': (8.100, 8.300),
    # ... modify as needed
}

strength_7d_ranges = {
    'M10': (214.00, 294.40),
    # ... modify as needed
}
```

## Troubleshooting

**Issue:** "ModuleNotFoundError: No module named 'pandas'"
- **Solution:** Run `pip install pandas openpyxl numpy`

**Issue:** Files not generating
- **Solution:** Ensure the `generated_data/` folder exists (created automatically) and you have write permissions


## Requirements

- pandas >= 1.0.0
- numpy >= 1.18.0
- openpyxl >= 3.0.0

## License

Free to use and modify for testing purposes.

---

**Version:** 1.3  
**Last Updated:** January 2026
