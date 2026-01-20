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

# ==== Renaming Columns ==== #
COLUMN_RENAME_MAP = None

# === Dropping Columns === # 
DROP_COLUMNS = ['source_of_data', 'Unnamed: 19', 'Unnamed: 20']

# ===== Converting Columns ===== #
CONVERT_TO_CATEGORICAL = [
    'country',
    'tier_distribution',
    'key_operators',
    'cloud_provider',
    'cooling_technologies_common',
    'regulatory_challenges_or_limits',
    'disaster_recovery_sites_common',
    'green_dc_initiatives_description'
]
CONVERT_TO_NUMERIC = [
    'total_data_centers',
    'hyperscale_data_centers',
    'colocation_data_centers',
    'floor_space_sqft_total',
    'power_capacity_MW_total',
    'internet_penetration_percent',
    'avg_latency_to_global_hubs_ms',
    'number_of_fiber_connections',
    'growth_rate_of_data_centers_percent_per_year'
]

# ===== ML CONFIG =====
# TARGET_COLUMN = 'growth_rate_of_data_centers_percent_per_year'
# FEATURE_COLUMNS = ['country' , 'total_data_centers', ]


# ===== Archieve =====
# NOTEBOOK_FILE = NOTEBOOK_DIR / "eda.ipynb"
# LIBRARY_FILE = SRC_DIR / "library.py"
# CONSTANTS_FILE = SRC_DIR / "constants.py"

# NOTEBOOK_FILE.touch(exist_ok=True)
# LIBRARY_FILE.touch(exist_ok=True)
# CONSTANTS_FILE.touch(exist_ok=True)
