from . import load_csv

def load_kbo_batting(**kwargs):
    return load_csv("kbo_batting", **kwargs)

def load_kbo_pitching(**kwargs):
    return load_csv("kbo_pitching", **kwargs)

def load_npb_batting(**kwargs):
    return load_csv("npb_batting", **kwargs)

def load_npb_pitching(**kwargs):
    return load_csv("npb_pitching", **kwargs)

__all__ = [
    "load_kbo_batting",
    "load_kbo_pitching",
    "load_npb_batting",
    "load_npb_pitching",
]
