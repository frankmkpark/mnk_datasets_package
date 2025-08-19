from . import load_csv

# sNK
def load_nk_batting(**kwargs):
    return load_csv("nk_batting", **kwargs)

def load_nk_pitching(**kwargs):
    return load_csv("nk_pitching", **kwargs)

def load_mnk_fielding(**kwargs):
    return load_csv("nk_fielding", **kwargs)

def load_nk_people(**kwargs):
    return load_csv("nk_people", **kwargs)

def load_nk_league(**kwargs):
    return load_csv("nk_league", **kwargs)

def load_nk_team(**kwargs):
    return load_csv("nk_team", **kwargs)

def load_nk_merged_people(**kwargs):
    return load_csv("merged_player_records", **kwargs)

__all__ = [
    "load_nk_batting",
    "load_nk_pitching",
    "load_nk_fielding",
    "load_nk_people",
    "load_nk_league",
    "load_nk_team",
    "load_nk_merged_people",
    ]
