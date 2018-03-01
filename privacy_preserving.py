import numpy as np
from zlib import crc32


class Preserve(object):
    def __init__(self, dataframe, jitter=2):
        self._jitter = jitter
        self._data = dataframe

    def _protect(self, val, query):
        np.random.seed(crc32(query.encode()))

        if val <= self._jitter:
            jitter_range = (0, (self._jitter * 2) + 1)
        else:
            jitter_range = (val - self._jitter, val + self._jitter + 1)

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
