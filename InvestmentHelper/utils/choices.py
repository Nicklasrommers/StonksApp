import csv
import os

DATASET_PATH = os.path.join(os.path.dirname(__file__), '..', 'dataset', 'assets.csv')


def get_label_name(string):
    return string.replace('_', ' ').capitalize()


class ModelChoices:
    def __init__(self, choices_list, include_all=True):
        self._choices = []
        if include_all:
            self._choices.append(('all', 'All'))
        for item in sorted({str(choice) for choice in choices_list if str(choice).strip()}):
            self._choices.append((item, get_label_name(item)))

    def choices(self):
        return self._choices


def _read_assets():
    if not os.path.exists(DATASET_PATH):
        return []
    with open(DATASET_PATH, newline='', encoding='utf-8') as csv_file:
        return list(csv.DictReader(csv_file))


assets = _read_assets()

AssetTypeChoices = ModelChoices([row['asset_type'] for row in assets])
AssetCountryChoices = ModelChoices([row['country'] for row in assets])
AssetSectorChoices = ModelChoices([row['sector'] for row in assets])
RiskLevelChoices = ModelChoices(['1', '2', '3', '4', '5'])
RequiredRiskLevelChoices = ModelChoices(['1', '2', '3', '4', '5'], include_all=False)
