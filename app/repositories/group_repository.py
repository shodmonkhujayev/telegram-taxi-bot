from pathlib import Path


class GroupRepository:

    def __init__(self):
        self.file = Path("groups.txt")

    def get_all(self) -> list[int]:

        if not self.file.exists():
            return []

        groups = []

        for line in self.file.read_text().splitlines():

            line = line.strip()

            if not line:
                continue

            if line.startswith("#"):
                continue

            groups.append(int(line))

        return groups


group_repository = GroupRepository()
