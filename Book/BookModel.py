class BookModel:
    def __init__(self, title=None):
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if title is not None:
            self._title = title
        else:
            # todo error file
            raise ValueError('Invalid title')

