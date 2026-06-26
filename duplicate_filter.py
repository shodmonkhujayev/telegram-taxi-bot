import time


class DuplicateFilter:

    def __init__(self, ttl=600):
        self.ttl = ttl
        self.cache = {}

    def is_duplicate(self, text: str) -> bool:

        now = time.time()

        self.cleanup()

        key = text.strip().lower()

        if key in self.cache:
            return True

        self.cache[key] = now

        return False

    def cleanup(self):

        now = time.time()

        expired = []

        for key, timestamp in self.cache.items():
            if now - timestamp > self.ttl:
                expired.append(key)

        for key in expired:
            del self.cache[key]


duplicate_filter = DuplicateFilter()
