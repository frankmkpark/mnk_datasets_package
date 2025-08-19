"""
Collections (flat layout):
- kbo_npb
- kbo_npb_mlb
- mnk_merged
- mnk_merged_tall

Each subpackage:
  - list_csv()
  - load_csv(csv_name, **read_csv_kwargs)
"""

from __future__ import annotations
import importlib

__version__ = "0.1.0"

_COLLECTION_PACKAGES = {
    "kbo_npb": "kbo_npb",
    "kbo_npb_mlb": "kbo_npb_mlb",
    "mnk_merged": "mnk_merged",
    "mnk_merged_tall": "mnk_merged_tall",
}

def show_collections() -> list[str]:
    return list(_COLLECTION_PACKAGES.keys())

def _get_pkg_module(collection: str):
    try:
        pkg_name = _COLLECTION_PACKAGES[collection]
    except KeyError:
        raise KeyError(f"Unknown collection: {collection}. Available: {show_collections()}")
    return importlib.import_module(pkg_name)

def list_csv(collection: str) -> list[str]:
    return _get_pkg_module(collection).list_csv()

def load_csv(collection: str, csv_name: str, **read_csv_kwargs):
    return _get_pkg_module(collection).load_csv(csv_name, **read_csv_kwargs)

# --- Convenience loaders (MNK core in kbo_npb_mlb) ---
from kbo_npb_mlb.api import (
    load_mnk_people,
    load_mnk_batting,
    load_mnk_pitching,
    load_mnk_fielding,
)

# --- Extras from mnk_merged_tall ---
from mnk_merged_tall.api import (
    load_mnk_playerstats,
    load_mnk_league,
    load_mnk_team,
    load_mnk_stats,
)

__all__ = [
    "show_collections",
    "list_csv",
    "load_csv",
    "load_mnk_people",
    "load_mnk_batting",
    "load_mnk_pitching",
    "load_mnk_fielding",
    "load_mnk_playerstats",
    "load_mnk_league",
    "load_mnk_team",
    "load_mnk_stats",
    "__version__",
]
