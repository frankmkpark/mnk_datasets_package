from importlib.resources import files, as_file
import pandas as pd
from pathlib import Path

def list_csv() -> list[str]:
    # list available CSVs in the kbo_npb_mlb collection
    base = files(__package__).joinpath("data")
    with as_file(base) as base_path:
        return [p.name for p in Path(base_path).glob("*.csv")]

def load_csv(csv_name, **kwargs) -> pd.DataFrame:
    # load a CSV from the kbo_npb_mlb collection into a DataFrame
    name = csv_name if csv_name.endswith(".csv") else f"{csv_name}.csv"
    resource = files(__package__).joinpath("data").joinpath(name)
    with as_file(resource) as path:
        return pd.read_csv(path, **kwargs)

__all__ = ["list_csv", "load_csv"]
