import sys
from pathlib import Path
from dotenv import load_dotenv

# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Make `app` importable
sys.path.insert(0, str(PROJECT_ROOT))

# Load .env from project root
load_dotenv(dotenv_path=PROJECT_ROOT / ".env")
