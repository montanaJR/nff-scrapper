from __future__ import annotations
from typing import List


class FileExportContext:
    def __init__(self, strategy):
        self._strategy = strategy

    def export(self, data: List):
        self._strategy.do(data)
