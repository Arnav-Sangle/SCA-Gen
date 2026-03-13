import pandas as pd

REQUIRED_COLUMNS = [
    "Component",
    "Publisher",
    "Version"
]


def parse_excel(file):

    df = pd.read_excel(file)

    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise Exception(f"Missing required columns: {missing}")

    df = df.fillna("")

    return df