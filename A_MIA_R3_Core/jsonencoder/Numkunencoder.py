import json

import numpy


class Numkunencoder(json.JSONEncoder):
    """
    JSONにエクスポートするときに使うエンコーダー
    """
    def default(self, obj):
        if isinstance(obj,numpy.floating):
            return float(obj)
        else:
            return super(Numkunencoder,self).default(obj)
