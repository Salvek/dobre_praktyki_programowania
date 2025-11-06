import csv

def load_csv(path: str):
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)
