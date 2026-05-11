import pandas as pd
import numpy as np
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
    #df["valor_total"] = df["amount"].cumsum()

    logging.info("Iniciando CAMADA GOLD (regras de negócio)...")

    df = df.copy()

    df['date'] = pd.to_datetime(df['date'])

    df['DIA'] = df['date'].dt.day

    # Semana da fatura
    condicoes_semana = [
        (df['DIA'] >= 17) & (df['DIA'] <= 23),
        (df['DIA'] >= 24),
        (df['DIA'] <= 7),
        (df['DIA'] >= 8) & (df['DIA'] <= 16)
    ]

    valores_semana = [1, 2, 3, 4]
    df['SEMANA_FATURA'] = np.select(condicoes_semana, valores_semana, default=0)

    # MES_FATURA dinâmico
    df['MES_FATURA'] = df['date'].apply(lambda x: f"{(x + pd.DateOffset(days=15)).strftime('%Y-%m')}")

    GOLD_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(GOLD_PATH, index=False)

    logging.info(f"Dados salvos em GOLD: {GOLD_PATH}")

    return df