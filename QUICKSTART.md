# QUICK START GUIDE

## ✓ What's Ready

Your data generator is fully functional with all 10 Excel files already generated:

### Concrete Mixes (1000 rows each)
- `Concrete_M10.xlsx`
- `Concrete_M15.xlsx`
- `Concrete_M20.xlsx`
- `Concrete_M25.xlsx`
- `Concrete_M30.xlsx`
- `Concrete_M35.xlsx`
- `Concrete_M40.xlsx`
- `Concrete_M45.xlsx`

### Mortar Mixes (1000 rows each)
- `Mortar_1_4.xlsx` (1:4 ratio)
- `Mortar_1_6.xlsx` (1:6 ratio)

All files are in the `generated_data/` folder with verified data ranges ✓

---

## 📋 How to Use

### Option 1: Run from Terminal (Linux/Mac)
```bash
python3 data_generator.py
```

### Option 2: Run from Terminal (Windows)
```bash
python data_generator.py
```

Or double-click `run.bat`

### Option 3: Run Executable (Windows Only)
```bash
dist/DataGenerator.exe
```

### Option 4: Preview Data
```bash
python3 preview_data.py
```

---

## 🎯 Menu Options When Running

The script presents 4 options:

```
[1] Generate All Concrete Mixes (M10-M45)
    - Creates 8 files, 1000 rows each
    - Takes ~30 seconds

[2] Generate Single Concrete Mix
    - Choose specific mix (M10-M45)
    - Choose custom row count
    - Creates 1 file

[3] Generate Mortar Data (1:4 and 1:6)
    - Creates 2 mortar files
    - Choose custom row count
    - Takes ~10 seconds

[4] Exit
    - Closes the program
```

---

## 📊 Data Quality Verified

✓ All 1000 rows per file verified  
✓ Weight values unique within each row  
✓ All ranges match specifications  
✓ Strength values properly distributed  
✓ Excel format ready for use  

---

## 🔧 Converting to EXE (If Needed)

Windows executable is already built at: `dist/DataGenerator.exe`

To rebuild:
```bash
python build_exe.py
```

Or manually:
```bash
pyinstaller --onefile --console data_generator.py
```

---

## 📁 File Structure

```
/workspace
├── data_generator.py          # Main script
├── build_exe.py               # Build script for EXE
├── preview_data.py            # Preview verification script
├── run.sh                      # Linux/Mac launcher
├── run.bat                     # Windows launcher
├── README.md                   # Full documentation
├── QUICKSTART.md             # This file
│
├── generated_data/            # Output folder
│   ├── Concrete_M10.xlsx
│   ├── Concrete_M15.xlsx
│   ├── ... (all files)
│   └── Mortar_1_6.xlsx
│
├── dist/                      # Executable
│   └── DataGenerator.exe
│
└── build/                     # Build artifacts
```

---

## 📝 Sample Data (From Verification)

**M20 Concrete - Row 1:**
- Weights: 8.190, 8.159, 8.272, 8.214, 8.166, 8.201
- 7-Day Strength: 366.13-408.09 MPa range
- 28-Day Strength: 547.11-589.09 MPa range

**Mortar 1:4 - Row 1:**
- Weights: 0.831, 0.800, 0.827, 0.812, 0.816, 0.801
- 7-Day Strength: 25.20-33.90 MPa range
- 28-Day Strength: 40.60-50.10 MPa range

---

## ⚙️ Requirements

- Python 3.7+ (for script)
- pandas, numpy, openpyxl (installed automatically)
- No additional requirements for EXE

---

## 🚀 Next Steps

1. **Open Excel Files:** Browse `generated_data/` and open any file
2. **Generate More:** Run `python data_generator.py` anytime
3. **Customize:** Edit ranges in `data_generator.py` if needed
4. **Share:** Copy `dist/DataGenerator.exe` to distribute

---

## ❓ Troubleshooting

**Problem:** Python command not found  
**Solution:** Use `python3` instead of `python`

**Problem:** Module not found error  
**Solution:** Run `pip install pandas openpyxl numpy`

**Problem:** Permission denied (Linux)  
**Solution:** Run `chmod +x run.sh` then `./run.sh`

---

**Version:** 1.0  
**Status:** ✓ Ready to Use  
**Date:** January 2026
