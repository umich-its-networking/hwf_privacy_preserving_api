import pandas as pd


class Preserve(object):

    _df = None

    def __init__(self):
        pass


class PreserveCsv(Preserve):

    def __init__(self, csv_file_path, **kw_args):
        self._df = pd.read_csv(csv_file_path, **kw_args)

    def count(self, query):
        return len(self._df.query(query))
