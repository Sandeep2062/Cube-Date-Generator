"""
Build script to convert data_generator.py to standalone exe using PyInstaller
Run this script from command line: python build_exe.py
"""

import subprocess
import sys
import os

def build_exe():
    """Build executable using PyInstaller"""
    
    print("Building executable with PyInstaller...")
    print("="*60)
    
    command = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",  # Create single exe file
        "--windowed",  # No console window (remove this if you want console)
        "--name", "DataGenerator",
        "--distpath", "./dist",
        "--buildpath", "./build",
        "--specpath", "./build",
        "--icon=NONE",
        "data_generator.py"
    ]
    
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✓ Build successful!")
            print("\nExecutable location:")
            exe_path = os.path.join("dist", "DataGenerator.exe" if sys.platform == "win32" else "DataGenerator")
            print(f"  {exe_path}")
            print("\nYou can now run the executable directly or include it in your project.")
        else:
            print("✗ Build failed!")
            print("\nError output:")
            print(result.stderr)
    
    except Exception as e:
        print(f"✗ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    build_exe()
