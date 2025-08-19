from . import load_csv

# MNK
def load_mnk_playerstats(**kwargs):
    return load_csv("mnk_playerstats", **kwargs)

def load_mnk_league(**kwargs):
    return load_csv("mnk_league", **kwargs)

def load_mnk_team(**kwargs):
    return load_csv("mnk_team", **kwargs)

def load_mnk_stats(**kwargs):
    return load_csv("mnk_stats", **kwargs)

__all__ = [
    "load_mnk_playerstats",
    "load_mnk_stats",
    "load_mnk_league",
    "load_mnk_team",
    ]
