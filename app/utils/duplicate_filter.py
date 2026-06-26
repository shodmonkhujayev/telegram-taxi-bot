class DuplicateFilter:

    def __init__(self):
        self.cache = set()

    def is_duplicate(self, text: str) -> bool:

        text = text.strip().lower()

        if text in self.cache:
            return True

        self.cache.add(text)
        return False


duplicate_filter = DuplicateFilter()
