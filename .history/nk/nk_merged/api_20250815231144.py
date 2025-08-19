from . import load_csv

# MNK
def load_mnk_batting(**kwargs):
    return load_csv("mnk_batting", **kwargs)

def load_mnk_pitching(**kwargs):
    return load_csv("mnk_pitching", **kwargs)

def load_mnk_fielding(**kwargs):
    return load_csv("mnk_fielding", **kwargs)

def load_mnk_people(**kwargs):
    return load_csv("mnk_people", **kwargs)

def load_mnk_league(**kwargs):
    return load_csv("mnk_league", **kwargs)

def load_mnk_team(**kwargs):
    return load_csv("mnk_team", **kwargs)

def load_mnk_merged_people(**kwargs):
    return load_csv("merged_player_records", **kwargs)

__all__ = [
    "load_mnk_batting",
    "load_mnk_pitching",
    "load_mnk_fielding",
    "load_mnk_people",
    "load_mnk_league",
    "load_mnk_team",
    "load_mnk_merged_people",
    ]
