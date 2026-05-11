import logging
from extract import extract
from transform import transform, business
from load import load

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_pipeline():
    df = extract()
    df = transform(df)
    df = business(df)
    load(df)

if __name__ == "__main__":
    run_pipeline()