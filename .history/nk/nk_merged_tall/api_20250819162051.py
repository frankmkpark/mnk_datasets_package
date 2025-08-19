from . import load_csv

# NK tall
def load_nk_playerstats_CL (**kwargs):
    return load_csv("nk_playerstats_CL", **kwargs)

def load_nk_playerstats_JBL (**kwargs):
    return load_csv("nk_playerstats_JBL", **kwargs)

def load_nk_playerstats_KBO (**kwargs):
    return load_csv("nk_playerstats_KBO", **kwargs)

def load_nk_playerstats_PL (**kwargs):
    return load_csv("nk_playerstats_PL", **kwargs)

def load_nk_league(**kwargs):
    return load_csv("nk_league", **kwargs)

def load_nk_team(**kwargs):
    return load_csv("nk_team", **kwargs)

def load_nk_stats(**kwargs):
    return load_csv("nk_stats", **kwargs)

__all__ = [
    "load_mnk_playerstats_AA",
    "load_mnk_playerstats_AL_firsthalf",
    "load_mnk_playerstats_AL_secondhalf",
    "load_mnk_playerstats_CL",
    "load_mnk_playerstats_FL",
    "load_mnk_playerstats_JBL",
    "load_mnk_playerstats_KBO",
    "load_mnk_playerstats_NAN",
    "load_mnk_playerstats_NL_firsthalf",
    "load_mnk_playerstats_NL_secondhalf",
    "load_mnk_playerstats_PL",
    "load_mnk_playerstats_UA",
    "load_mnk_playerstats_UPL",
    "load_mnk_stats",
    "load_mnk_league",
    "load_mnk_team",
    ]
