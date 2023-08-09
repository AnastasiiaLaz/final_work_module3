from pathlib import Path

"""
путь из данного файла к файлу operations.json
"""

ROOT_PATH = Path(__file__).parent
PATH_TO_JSON = Path.joinpath(ROOT_PATH, 'arrs', 'settings', 'operations.json')
