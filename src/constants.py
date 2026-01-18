from pathlib import Path
from enum import Enum

# ===== PROJECT ROOT =====
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# ===== DIRECTORIES =====
DATA_DIR = PROJECT_ROOT / "data"
MODEL_DIR = PROJECT_ROOT / "model"
IMAGE_DIR = PROJECT_ROOT / "img"
NOTEBOOK_DIR = PROJECT_ROOT / "notebook"
SRC_DIR = PROJECT_ROOT / "src"

# ==== If needed, create  ==== #
DATA_DIR.mkdir(exist_ok=True)
MODEL_DIR.mkdir(exist_ok=True) 
IMAGE_DIR.mkdir(exist_ok=True) 
NOTEBOOK_DIR.mkdir(exist_ok=True)
SRC_DIR.mkdir(exist_ok=True)

# ===== CSV FILES (explicit) ===== 
CSV_FILE = list(DATA_DIR.glob("*.csv"))[0]

# === Columns to Drop === # 
DROP_COLUMNS = ['source_of_data', 'Unnamed: 19', 'Unnamed: 20']

# ===== ML CONFIG =====
TARGET_COLUMN = None
FEATURE_COLUMNS = None


# ===== Archieve =====
# NOTEBOOK_FILE = NOTEBOOK_DIR / "eda.ipynb"
# LIBRARY_FILE = SRC_DIR / "library.py"
# CONSTANTS_FILE = SRC_DIR / "constants.py"

# NOTEBOOK_FILE.touch(exist_ok=True)
# LIBRARY_FILE.touch(exist_ok=True)
# CONSTANTS_FILE.touch(exist_ok=True)
