import pandas as pd
import logging
from config import RAW_FOLDER, BRONZE_PATH
from pathlib import Path

def extract():
    logging.info("Iniciando EXTRAÇÃO (BRONZE)...")

    arquivos = list(Path(RAW_FOLDER).glob("*.csv"))
    if not arquivos:
        raise FileNotFoundError("Nenhum CSV encontrado na pasta raw")

    dfs = [pd.read_csv(file) for file in arquivos]
    df = pd.concat(dfs, ignore_index=True)

    BRONZE_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(BRONZE_PATH, index=False)

    logging.info(f"Dados salvos em BRONZE: {BRONZE_PATH}")
    return df