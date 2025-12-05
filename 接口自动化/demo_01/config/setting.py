from pathlib import Path
import yaml

BASE_DIR = Path(__file__).parent
CONFIG_FILE = BASE_DIR / 'config.yaml'

def load_config():
    with open(CONFIG_FILE, 'r') as f:
        return yaml.safe_load(f)
