import pandas as pd
import numpy as np
from zlib import crc32


class Preserve(object):
    def __init__(self, dataframe):
        self._data = dataframe

    def _protect(self, val, query):
        jitter = 2
        np.random.seed(crc32(query.encode()))

        if val <= jitter:
            jitter_range = (0, (jitter * 2) + 1)
        else:
            jitter_range = (val - jitter, val + jitter + 1)

        protected_val = np.random.randint(*jitter_range)

        return protected_val

    def attributes(self):
        return dict(zip(
            self._data.columns,
            list(map(str, list(self._data.dtypes)))
        ))

    def count(self, query):
        return self._protect(
            len(self._data.query(query)),
            query
        )


class PreserveCsv(Preserve):

    def __init__(self, *args, **kw_args):
        return pd.read_csv(*args, **kw_args)
