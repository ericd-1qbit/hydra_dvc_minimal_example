class MyModel(object):
    def __init__(self, name=None) -> None:
        super().__init__()

        self._name = name

    def __str__(self) -> str:
        return self._name
