"""
Collections (flat layout):
- kbo_npb
- kbo_npb_mlb
- mnk_merged
- mnk_merged_tall

Each subpackage exposes:
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

def show_collections():
    # list available dataset collections
    return list(_COLLECTION_PACKAGES.keys())

def _get_pkg_module(collection):
    try:
        pkg_name = _COLLECTION_PACKAGES[collection]
    except KeyError:
        raise KeyError(f"Unknown collection: {collection}. Available: {show_collections()}")
    return importlib.import_module(pkg_name)

def list_csv(collection):
    # list CSV files available in a collection
    return _get_pkg_module(collection).list_csv()

def load_csv(collection, csv_name, **read_csv_kwargs):
    # load a CSV into a pandas DataFrame
    return _get_pkg_module(collection).load_csv(csv_name, **read_csv_kwargs)

# KBO+NPB loaders
from kbo_npb.api import (
    load_kbo_batting,
    load_kbo_pitching,
    load_kbo_fielding,
    load_kbo_people,
    load_npb_batting,
    load_npb_pitching,
    load_npb_fielding,
    load_npb_people,
)

# KBO+NPB+MLB loaders
from kbo_npb_mlb.api import (
    load_kbo_batting as load_kbo_batting_aligned,
    load_kbo_pitching as load_kbo_pitching_aligned,
    load_kbo_fielding as load_kbo_fielding_aligned,
    load_kbo_people as load_kbo_people_aligned,
    load_npb_batting as load_npb_batting_aligned,
    load_npb_pitching as load_npb_pitching_aligned,
    load_npb_fielding as load_npb_fielding_aligned,
    load_npb_people as load_npb_people_aligned,
    load_mlb_batting as load_mlb_batting_aligned,
    load_mlb_pitching as load_mlb_pitching_aligned,
    load_mlb_fielding as load_mlb_fielding_aligned,
    load_mlb_people as load_mlb_people_aligned,
)

# MNK merged loaders
from mnk_merged.api import (
    load_mnk_batting,
    load_mnk_pitching,
    load_mnk_fielding,
    load_mnk_people,
    load_mnk_league,
    load_mnk_team,
    load_mnk_merged_people,
)

# MNK merged tall loaders
from mnk_merged_tall.api import (
    load_mnk_playerstats,
    load_mnk_league as load_mnk_league_tall,
    load_mnk_team as load_mnk_team_tall,
    load_mnk_stats,
)

__all__ = [
    # interface
    "show_collections",
    "list_csv",
    "load_csv",

    # KBO+NPB
    "load_kbo_batting",
    "load_kbo_pitching",
    "load_kbo_fielding",
    "load_kbo_people",
    "load_npb_batting",
    "load_npb_pitching",
    "load_npb_fielding",
    "load_npb_people",

    # KBO+NPB+MLB
    "load_kbo_batting_aligned",
    "load_kbo_pitching_aligned",
    "load_kbo_fielding_aligned",
    "load_kbo_people_aligned",
    "load_npb_batting_aligned",
    "load_npb_pitching_aligned",
    "load_npb_fielding_aligned",
    "load_npb_people_aligned",
    "load_mlb_batting_aligned",
    "load_mlb_pitching_aligned",
    "load_mlb_fielding_aligned",
    "load_mlb_people_aligned",

    # MNK merged
    "load_mnk_batting",
    "load_mnk_pitching",
    "load_mnk_fielding",
    "load_mnk_people",
    "load_mnk_league",
    "load_mnk_team",
    "load_mnk_merged_people",

    # MNK merged tall
    "load_mnk_playerstats",
    "load_mnk_league_tall",
    "load_mnk_team_tall",
    "load_mnk_stats",

    "__version__",
]