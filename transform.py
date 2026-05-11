import pandas as pd
import logging
from config import SILVER_PATH, GOLD_PATH

def transform(df):
    logging.info("Iniciando TRANSFORMAÇÃO (SILVER)...")

    df = df.copy()

    # exemplo de limpeza
    df.dropna(inplace=True)

    SILVER_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(SILVER_PATH, index=False)

    logging.info(f"Dados salvos em SILVER: {SILVER_PATH}")
    return df


def business(df):
    logging.info("Iniciando REGRA DE NEGÓCIO (GOLD)...")

    df = df.copy()

    # exemplo de métrica
    df["valor_total"] = df["amount"].cumsum()


    GOLD_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(GOLD_PATH, index=False)

    logging.info(f"Dados salvos em GOLD: {GOLD_PATH}")
    return df