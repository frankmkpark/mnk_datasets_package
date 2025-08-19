# src/__init__.py
from typing import Dict, Callable
import importlib

# map the public collection names to their package modules
_COLLECTION_PKGS: Dict[str, str] = {
    "KBO+NPB": "kbo_npb",
    "KBO+NPB+MLB": "kbo_npb_mlb",
    "MNK_merged": "mnk_merged",
    "MNK_merged_tall": "mnk_merged_tall",
}

def collections() -> list[str]:
    """List available dataset collections (human-friendly names)."""
    return list(_COLLECTION_PKGS.keys())

def _get_pkg_module(collection: str):
    """Import the package module for a collection (must expose list_csvs/load_csv)."""
    try:
        pkg_name = _COLLECTION_PKGS[collection]
    except KeyError:
        raise KeyError(f"Unknown collection: {collection}. Options: {collections()}")
    return importlib.import_module(pkg_name)  # e.g., import kbo_npb

def list_csvs(collection: str) -> list[str]:
    """List CSV files available in a collection."""
    mod = _get_pkg_module(collection)
    return mod.list_csvs()

def load_csv(collection: str, csv_name: str, **read_csv_kwargs):
    """Load a CSV from a collection into a pandas DataFrame."""
    mod = _get_pkg_module(collection)
    return mod.load_csv(csv_name, **read_csv_kwargs)

# --- MNK core convenience loaders (always from KBO+NPB+MLB) -------------------
from kbo_npb_mlb.api import (
    load_mnk_people,
    load_mnk_batting,
    load_mnk_pitching,
    load_mnk_fielding,
)

# include if you’re shipping this large file in the package:
try:
    from kbo_npb_mlb.api import load_mnk_playerstats  # optional
except Exception:  # pragma: no cover
    def load_mnk_playerstats(**_):  # graceful fallback if not present
        raise ImportError("mnk_playerstats loader not available in this build.")

__all__ = [
    "collections",
    "list_csvs",
    "load_csv",
    "load_mnk_people",
    "load_mnk_batting",
    "load_mnk_pitching",
    "load_mnk_fielding",
    "load_mnk_playerstats",
]
