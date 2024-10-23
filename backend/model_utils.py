import joblib
from pathlib import Path


def load_model(path):
    path = Path(path)

    if not path.is_file():
        raise ValueError(f'File {path} does not exist')

    return joblib.load(path)
