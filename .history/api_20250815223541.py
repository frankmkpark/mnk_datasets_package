from importlib.resources import files, as_file
from pathlib import Path
import pandas as pd

_COLLECTION_MAP = {
    "KBO+NPB": "kbo_npb",
    "KBO+NPB+MLB": "kbo_npb_mlb",
    "MNK_merged": "mnk_merged",
    "MNK_mergged_tall": "mnk_mergged_tall",}

def collections() -> list[str]:
    return list(_COLLECTION_MAP.keys())

def list_csvs(collection: str) -> list[str]:
    if collection not in _COLLECTION_MAP:
        raise KeyError(f"Unknown collection: {collection}")
    pkg = _COLLECTION_MAP[collection]
    base = files(f"mnk_datasets.{pkg}").joinpath("data")
    with as_file(base) as base_path:
        return [p.name for p in Path(base_path).glob("*.csv")]

def load_csv(collection: str, csv_name: str, **read_csv_kwargs) -> pd.DataFrame:
    """
    csv_name: either 'kbo_batting.csv' or 'kbo_batting' ('.csv' optional)
    """
    if collection not in _COLLECTION_MAP:
        raise KeyError(f"Unknown collection: {collection}")
    name = csv_name if csv_name.endswith(".csv") else f"{csv_name}.csv"
    pkg = _COLLECTION_MAP[collection]
    resource = files(f"mnk_datasets.{pkg}").joinpath("data").joinpath(name)
    with as_file(resource) as path:
        return pd.read_csv(path, **read_csv_kwargs)
