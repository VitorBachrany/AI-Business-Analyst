import pandas as pd

_current_dataset = None


def set_dataset(df: pd.DataFrame):
    global _current_dataset
    _current_dataset = df


def get_dataset() -> pd.DataFrame | None:
    return _current_dataset


def clear_dataset():
    global _current_dataset
    _current_dataset = None