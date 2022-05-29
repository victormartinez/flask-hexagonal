from typing import List


class TemplatesException(Exception):

    @property
    def message(self) -> str:
        raise NotImplementedError("'Exception.message' not implemented.")

    @property
    def details(self) -> List[str]:
        raise NotImplementedError("'Exception.details' not implemented.")
