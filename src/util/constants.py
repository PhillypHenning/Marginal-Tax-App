import src.util.logger as pylog

import os, pathlib, glob

def ensure_dir(file_path):
    fp = pathlib.Path(file_path)
    if not fp.exists(): fp.mkdir(parents=True)

def clean_dir(file_path):
    files = glob.glob("{}/*".format(file_path))
    for f in files:
        os.remove(f)

# ENVIRONMENT VARIABLES
DATA_DIR = os.environ.get("DATA_DIR", "./data")
LOGS_DIR = "{}/logs".format(DATA_DIR)
ENVIRONMENT = os.environ.get("ENVIRONMENT", 'local')

# AUTHENTICATION
VALID_YEARS = [2019, 2020]


# Calculate Tax Bracket API
CTB_API_ADDRESS = os.environ.get("CTB_API_ADDRESS", "http://192.168.2.71")
CTB_API_PORT = os.environ.get("CTB_API_PORT", "5000")
CTB_API_URL = "{}:{}".format(CTB_API_ADDRESS, CTB_API_PORT)
CTB_API_ROUTE = 'tax-calculator/brackets'

# Ensure folder creation
ensure_dir(DATA_DIR)
ensure_dir(LOGS_DIR)

# Cleaning


# Logger start
logger = pylog.get_logger("Calculate-Income-Tax-App",log_dir='{}/logs'.format(DATA_DIR))