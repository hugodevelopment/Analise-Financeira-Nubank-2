from pathlib import Path

BASE_DIR = Path(__file__).parent

# Pastas
DATA_DIR = BASE_DIR / "data"
RAW_FOLDER = "RAW_FOLDER"
BRONZE_PATH = DATA_DIR / "bronze" / "dados.csv"
SILVER_PATH = DATA_DIR / "silver" / "dados_tratados.csv"
GOLD_PATH = DATA_DIR / "gold" / "dados_analiticos.csv"

# Colunas
COLUNA_DATA = "data"