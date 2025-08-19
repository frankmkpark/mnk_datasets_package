from . import load_csv

# NK tall

def load_mnk_playerstats_AL_secondhalf (**kwargs):
    return load_csv("mnk_playerstats_AL_secondhalf", **kwargs)

def load_mnk_playerstats_CL (**kwargs):
    return load_csv("mnk_playerstats_CL", **kwargs)

def load_mnk_playerstats_FL (**kwargs):
    return load_csv("mnk_playerstats_FL", **kwargs)

def load_mnk_playerstats_JBL (**kwargs):
    return load_csv("mnk_playerstats_JBL", **kwargs)

def load_mnk_playerstats_KBO (**kwargs):
    return load_csv("mnk_playerstats_KBO", **kwargs)

def load_mnk_playerstats_NAN (**kwargs):
    return load_csv("mnk_playerstats_NAN", **kwargs)

def load_mnk_playerstats_NL_firsthalf (**kwargs):
    return load_csv("mnk_playerstats_NL_firsthalf", **kwargs)

def load_mnk_playerstats_NL_secondhalf (**kwargs):
    return load_csv("mnk_playerstats_NL_secondhalf", **kwargs)

def load_mnk_playerstats_PL (**kwargs):
    return load_csv("mnk_playerstats_PL", **kwargs)

def load_mnk_playerstats_UA (**kwargs):
    return load_csv("mnk_playerstats_UA", **kwargs)

def load_mnk_playerstats_UPL (**kwargs):
    return load_csv("mnk_playerstats_UPL", **kwargs)

def load_mnk_league(**kwargs):
    return load_csv("mnk_league", **kwargs)

def load_mnk_team(**kwargs):
    return load_csv("mnk_team", **kwargs)

def load_mnk_stats(**kwargs):
    return load_csv("mnk_stats", **kwargs)

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
