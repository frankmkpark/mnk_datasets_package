"""
Subpackages:
- kbo_npb
- kbo_npb_mlb
- mnk_merged
- mnk_merged_tall

Each subpackage contains:
  - list_csv()
  - load_csv(csv_name, **read_csv_kwargs)
"""

from __future__ import annotations
from typing import Dict
import importlib

__version__ = "0.1.0"

_COLLECTION_PACAKGES = {
    "kbo_npb": "kbo_npb",
    "kbo_npb_mlb": "kbo_npb_mlb",
    "mnk_merged": "mnk_merged",
    "mnk_merged_tall": "mnk_merged_tall",
}

def show_collections():
    # list available dataset collections (public names)
    return list(_COLLECTION_PACAKGES.keys())

def _get_pkg_module(collection):
    try:
        pkg_name = _COLLECTION_PACAKGES[collection]
    except KeyError:
        raise KeyError(f"Unknown collection: {collection}. Available: {show_collections()}")
    return importlib.import_module(pkg_name)

def list_csv(collection):
    # list CSV files available in a collection
    mod = _get_pkg_module(collection)
    return mod.list_csv()

def load_csv(collection: str, csv_name: str, **read_csv_kwargs):
    """Load a CSV from a collection into a pandas DataFrame."""
    mod = _get_pkg_module(collection)
    return mod.load_csv(csv_name, **read_csv_kwargs)

# --- Convenience re-exports ---------------------------------------------------
# KBO+NPB+MLB core MNK files (always refer to these across the project)
try:
    from kbo_npb_mlb.api import (
        load_mnk_people,
        load_mnk_batting,
        load_mnk_pitching,
        load_mnk_fielding,
    )
except Exception as _e:  # pragma: no cover
    # provide clear errors if someone calls these without the module present
    def _missing(*_, **__):
        raise ImportError("kbo_npb_mlb.api MNK loaders are unavailable in this build.") from _e
    load_mnk_people = load_mnk_batting = load_mnk_pitching = load_mnk_fielding = _missing  # type: ignore

# MNK_merged_tall helpers you defined (playerstats, league, team, stats)
try:
    from mnk_merged_tall.api import (
        load_mnk_playerstats,
        load_mnk_league,
        load_mnk_team,
        load_mnk_stats,
    )
except Exception as _e:  # pragma: no cover
    def _missing_mt(*_, **__):
        raise ImportError("mnk_merged_tall.api loaders are unavailable in this build.") from _e
    load_mnk_playerstats = load_mnk_league = load_mnk_team = load_mnk_stats = _missing_mt  # type: ignore

__all__ = [
    # unified interface
    "collections",
    "list_csv",
    "load_csv",
    # MNK core (KBO+NPB+MLB)
    "load_mnk_people",
    "load_mnk_batting",
    "load_mnk_pitching",
    "load_mnk_fielding",
    # MNK merged tall extras
    "load_mnk_playerstats",
    "load_mnk_league",
    "load_mnk_team",
    "load_mnk_stats",
    # meta
    "__version__",
]
